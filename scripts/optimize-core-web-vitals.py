#!/usr/bin/env python3
"""One-time Core Web Vitals optimization without changing the site's visual content."""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / 'assets' / 'images'
BUILD = ROOT / 'scripts' / 'build.py'
APP = ROOT / 'assets' / 'app.js'
CHECK = ROOT / 'scripts' / 'check.py'


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'Pattern not found: {label}')
    return text.replace(old, new, 1)


def make_webp(src_name, dst_name, max_width, quality):
    src = IMAGES / src_name
    dst = IMAGES / dst_name
    with Image.open(src) as im:
        im = ImageOps.exif_transpose(im)
        if im.width > max_width:
            ratio = max_width / im.width
            size = (max_width, round(im.height * ratio))
            im = im.resize(size, Image.Resampling.LANCZOS)
        if im.mode not in ('RGB', 'RGBA'):
            im = im.convert('RGBA' if 'A' in im.getbands() else 'RGB')
        im.save(dst, 'WEBP', quality=quality, method=6, exact=True)
        width, height = im.size
    print(f'{dst.name}: {width}x{height}, {dst.stat().st_size} bytes')
    return width, height


# Keep the exact photos/logos, only resize and encode them more efficiently.
logo_w, logo_h = make_webp('tugba-logo-yatay.png', 'tugba-logo-yatay-cwv.webp', 720, 88)
light_w, light_h = make_webp('tugba-logo-yatay-light.png', 'tugba-logo-yatay-light-cwv.webp', 720, 88)
hero_w, hero_h = make_webp('tugba-hero-orijinal.jpg', 'tugba-hero-cwv.webp', 1200, 90)

b = BUILD.read_text()
b = replace_once(b, "LOGO='tugba-logo-yatay.png'", "LOGO='tugba-logo-yatay-cwv.webp'", 'header logo')
b = replace_once(b, "LOGO_LIGHT='tugba-logo-yatay-light.png'", "LOGO_LIGHT='tugba-logo-yatay-light-cwv.webp'", 'footer logo')
b = replace_once(b, "'tugba-hero-orijinal.jpg':(1512,1320)", f"'tugba-hero-cwv.webp':({hero_w},{hero_h})", 'hero dimensions')
b = replace_once(b, "dims[LOGO]=(1977,762)", f"dims[LOGO]=({logo_w},{logo_h})", 'logo dimensions')
b = replace_once(b, "dims[LOGO_LIGHT]=(1977,762)", f"dims[LOGO_LIGHT]=({light_w},{light_h})", 'light logo dimensions')
b = replace_once(
    b,
    "w,h=dims.get(file,(480,360) if file.startswith('video-') else (1280,720));load='fetchpriority=\"high\"' if eager else 'loading=\"lazy\"'",
    "w,h=dims.get(file,(480,360) if file.startswith('video-') else (1280,720));load='loading=\"eager\" fetchpriority=\"high\"' if eager else 'loading=\"lazy\"'",
    'explicit eager loading'
)
b = replace_once(
    b,
    "img('tugba-hero-orijinal.jpg','Diyetisyen Tuğba Şeker Ağaç beyaz önlüğüyle dış mekânda','hero-portrait-original',eager=True)",
    "img('tugba-hero-cwv.webp','Diyetisyen Tuğba Şeker Ağaç beyaz önlüğüyle dış mekânda','hero-portrait-original',eager=True)",
    'homepage hero asset'
)

b = replace_once(
    b,
    "    doc=f'''<!doctype html><html lang=\"tr\"><head>",
    "    hero_preload=f'<link rel=\"preload\" as=\"image\" type=\"image/webp\" href=\"{path(\"/assets/images/tugba-hero-cwv.webp\")}\" fetchpriority=\"high\">' if route=='/' else ''\n    calculator_script=f'<script defer src=\"{path(\"/assets/calculator.js\")}\"></script>' if 'data-bmi-form' in body else ''\n    doc=f'''<!doctype html><html lang=\"tr\"><head>",
    'performance head variables'
)
b = replace_once(
    b,
    "<link rel=\"icon\" type=\"image/png\" sizes=\"768x768\" href=\"{path('/assets/images/'+FAVICON)}\">",
    "<link rel=\"icon\" type=\"image/svg+xml\" href=\"{path('/assets/favicon.svg')}\">",
    'lightweight favicon'
)
b = replace_once(
    b,
    "<link rel=\"stylesheet\" href=\"{path('/assets/style.css')}?v=prices-v1\">",
    "{hero_preload}<link rel=\"stylesheet\" href=\"{path('/assets/style.css')}?v=cwv-v1\"><link rel=\"stylesheet\" href=\"{path('/assets/polish.css')}?v=cwv-v1\">",
    'blocking stable CSS and hero preload'
)
b = replace_once(
    b,
    "<script defer src=\"{path('/assets/calculator.js')}\"></script><script defer src=\"{path('/assets/app.js')}?v=hero-original-v6\"></script>",
    "{calculator_script}<script defer src=\"{path('/assets/app.js')}?v=cwv-v1\"></script>",
    'conditional calculator script'
)
BUILD.write_text(b)

app = APP.read_text()
polish_loader = "const polish=document.createElement('link');\npolish.rel='stylesheet';\npolish.href='/assets/polish.css?v=hero-original-v6';\ndocument.head.appendChild(polish);\n\n"
if polish_loader not in app:
    raise SystemExit('Pattern not found: runtime polish.css loader')
APP.write_text(app.replace(polish_loader, '', 1))

# Add durable performance regression checks.
c = CHECK.read_text()
marker = "if errors:\n    print('\\n'.join(errors));raise SystemExit(1)"
perf_checks = r'''
# Core Web Vitals regression checks.
asset_limits={
    'assets/images/tugba-hero-cwv.webp':220_000,
    'assets/images/tugba-logo-yatay-cwv.webp':80_000,
    'assets/images/tugba-logo-yatay-light-cwv.webp':80_000,
}
for rel,limit in asset_limits.items():
    p=ROOT/rel
    if not p.exists():errors.append(f'Missing optimized asset: {rel}')
    elif p.stat().st_size>limit:errors.append(f'Optimized asset too large: {rel}={p.stat().st_size}')
for file,p in pages.items():
    text=file.read_text()
    if '/assets/polish.css?v=cwv-v1' not in text:errors.append(f'{file}: polish.css must be linked in head')
    if 'tugba-logo-yatay.png' in text or 'tugba-logo-yatay-light.png' in text:errors.append(f'{file}: legacy PNG logo reference')
    has_bmi='data-bmi-form' in text
    has_calc='/assets/calculator.js' in text
    if has_bmi!=has_calc:errors.append(f'{file}: calculator script loading mismatch')
home=(OUT/'index.html').read_text()
if 'rel="preload" as="image" type="image/webp" href="/assets/images/tugba-hero-cwv.webp" fetchpriority="high"' not in home:
    errors.append('Homepage hero preload missing')
if 'tugba-hero-orijinal.jpg' in home:errors.append('Homepage still references legacy hero JPEG')
'''
if perf_checks.strip() not in c:
    if marker not in c:
        raise SystemExit('Pattern not found: check.py error marker')
    c = c.replace(marker, perf_checks + '\n' + marker, 1)
CHECK.write_text(c)

print('Core Web Vitals source optimizations applied.')
