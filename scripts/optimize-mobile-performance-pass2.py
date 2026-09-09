#!/usr/bin/env python3
"""Second-pass mobile performance optimization without changing visible content."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'scripts' / 'build.py'
CHECK = ROOT / 'scripts' / 'check.py'


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'Pattern not found: {label}')
    return text.replace(old, new, 1)

b = BUILD.read_text()

# Inline the small homepage-only hero stylesheet so internal pages do not download it
# and the homepage does not wait for a second render-blocking CSS request.
anchor = "FAVICON='tugba-logo-ikon.png'\n"
if "HOME_CRITICAL_CSS=" not in b:
    b = replace_once(
        b,
        anchor,
        anchor + "HOME_CRITICAL_CSS=(ROOT/'assets/polish.css').read_text().replace('@charset \\\"UTF-8\\\";','',1).strip()\n",
        'home critical CSS constant'
    )

old_load = "    w,h=dims.get(file,(480,360) if file.startswith('video-') else (1280,720));load='loading=\"eager\" fetchpriority=\"high\"' if eager else 'loading=\"lazy\"'"
new_load = "    w,h=dims.get(file,(480,360) if file.startswith('video-') else (1280,720));load=('loading=\"eager\"' if file==LOGO else 'loading=\"eager\" fetchpriority=\"high\"') if eager else 'loading=\"lazy\" fetchpriority=\"low\"'"
b = replace_once(b, old_load, new_load, 'image priority separation')

old_head_vars = "    hero_preload=f'<link rel=\"preload\" as=\"image\" type=\"image/webp\" href=\"{path(\"/assets/images/tugba-hero-cwv.webp\")}\" fetchpriority=\"high\">' if route=='/' else ''\n    calculator_script=f'<script defer src=\"{path(\"/assets/calculator.js\")}\"></script>' if 'data-bmi-form' in body else ''"
new_head_vars = "    lcp_match=re.search(r'<img src=\"[^\"]*assets/images/([^\"]+)\"[^>]*loading=\"eager\" fetchpriority=\"high\"',body[:8000])\n    lcp_file='tugba-hero-cwv.webp' if route=='/' else (lcp_match.group(1) if lcp_match else '')\n    hero_preload=f'<link rel=\"preload\" as=\"image\" type=\"image/webp\" href=\"{path(\"/assets/images/\"+lcp_file)}\" fetchpriority=\"high\">' if lcp_file.endswith('.webp') else ''\n    home_critical=f'<style data-home-critical>{HOME_CRITICAL_CSS}</style>' if route=='/' else ''\n    calculator_script=f'<script defer src=\"{path(\"/assets/calculator.js\")}\"></script>' if 'data-bmi-form' in body else ''"
b = replace_once(b, old_head_vars, new_head_vars, 'LCP preload and inline home CSS')

old_assets = "{hero_preload}<link rel=\"stylesheet\" href=\"{path('/assets/style.css')}?v=cwv-v1\"><link rel=\"stylesheet\" href=\"{path('/assets/polish.css')}?v=cwv-v1\"><script type=\"application/ld+json\">"
new_assets = "{hero_preload}<link rel=\"stylesheet\" href=\"{path('/assets/style.css')}?v=cwv-v2\">{home_critical}<script type=\"application/ld+json\">"
b = replace_once(b, old_assets, new_assets, 'remove global polish request')

b = replace_once(
    b,
    "<script defer src=\"{path('/assets/app.js')}?v=cwv-v1\"></script>",
    "<script defer src=\"{path('/assets/app.js')}?v=cwv-v2\"></script>",
    'app cache version'
)
BUILD.write_text(b)

# Update regression checks for the second-pass loading architecture.
c = CHECK.read_text()
old_block = """for file,p in pages.items():
    text=file.read_text()
    if '/assets/polish.css?v=cwv-v1' not in text:errors.append(f'{file}: polish.css must be linked in head')
    if 'tugba-logo-yatay.png' in text or 'tugba-logo-yatay-light.png' in text:errors.append(f'{file}: legacy PNG logo reference')
    has_bmi='data-bmi-form' in text
    has_calc='/assets/calculator.js' in text
    if has_bmi!=has_calc:errors.append(f'{file}: calculator script loading mismatch')
home=(OUT/'index.html').read_text()
if 'rel=\"preload\" as=\"image\" type=\"image/webp\" href=\"/assets/images/tugba-hero-cwv.webp\" fetchpriority=\"high\"' not in home:
    errors.append('Homepage hero preload missing')
if 'tugba-hero-orijinal.jpg' in home:errors.append('Homepage still references legacy hero JPEG')
"""
new_block = """for file,p in pages.items():
    text=file.read_text()
    if '/assets/polish.css' in text:errors.append(f'{file}: polish.css should not be a render-blocking request')
    if 'tugba-logo-yatay.png' in text or 'tugba-logo-yatay-light.png' in text:errors.append(f'{file}: legacy PNG logo reference')
    has_bmi='data-bmi-form' in text
    has_calc='/assets/calculator.js' in text
    if has_bmi!=has_calc:errors.append(f'{file}: calculator script loading mismatch')
    if 'loading=\"lazy\"' in text and 'fetchpriority=\"low\"' not in text:errors.append(f'{file}: lazy images should be low priority')
    high=re.findall(r'<img src=\"([^\"]+)\"[^>]*loading=\"eager\" fetchpriority=\"high\"',text[:12000])
    for src in high:
        if f'<link rel=\"preload\" as=\"image\" type=\"image/webp\" href=\"{src}\" fetchpriority=\"high\">' not in text:
            errors.append(f'{file}: high-priority hero image must be preloaded: {src}')
home=(OUT/'index.html').read_text()
if 'rel=\"preload\" as=\"image\" type=\"image/webp\" href=\"/assets/images/tugba-hero-cwv.webp\" fetchpriority=\"high\"' not in home:
    errors.append('Homepage hero preload missing')
if '<style data-home-critical>' not in home:errors.append('Homepage critical hero CSS must be inline')
if 'tugba-hero-orijinal.jpg' in home:errors.append('Homepage still references legacy hero JPEG')
"""
c = replace_once(c, old_block, new_block, 'CWV regression block')
CHECK.write_text(c)

print('Second-pass mobile performance optimizations applied.')
