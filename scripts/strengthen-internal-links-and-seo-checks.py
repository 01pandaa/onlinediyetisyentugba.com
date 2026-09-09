#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
build = ROOT / 'scripts' / 'build.py'
check = ROOT / 'scripts' / 'check.py'


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'Pattern not found: {label}')
    return text.replace(old, new, 1)

# --- Strengthen contextual internal links in the generator ---
b = build.read_text()

old_sidebar = '''def sidebar():return f'<aside class="sidebar"><h3>Tanışalım.</h3><p>Online danışmanlık veya Adana ofisi için görüşme sürecini öğrenebilirsiniz.</p>{btn(WA,"WhatsApp ile iletişim")}{btn("tel:"+S["phone"],"Telefonla arayın",True)}<p>WhatsApp: {e(S["whatsapp_hours"])}<br>Pazar kapalı.</p><nav aria-label="İlgili sayfalar">{link("/online-diyetisyen/","Online danışmanlık süreci ↗")}{link("/vucudunu-tani/","Vücudunu Tanı ↗")}{link("/blog/","Diğer beslenme yazıları ↗")}</nav></aside>' '''.strip()
new_sidebar = '''def sidebar():return f'<aside class="sidebar"><h3>Tanışalım.</h3><p>Online danışmanlık veya Adana ofisi için görüşme sürecini öğrenebilirsiniz.</p>{btn(WA,"WhatsApp ile iletişim")}{btn("tel:"+S["phone"],"Telefonla arayın",True)}<p>WhatsApp: {e(S["whatsapp_hours"])}<br>Pazar kapalı.</p><nav aria-label="İlgili sayfalar">{link("/online-diyetisyen/","Online danışmanlık süreci ↗")}{link("/online-diyetisyen-fiyatlari/","Online diyetisyen fiyatları ↗")}{link("/hizmetler/","Hizmet alanları ↗")}{link("/sikca-sorulan-sorular/","Sık sorulan sorular ↗")}{link("/blog/","Diğer beslenme yazıları ↗")}</nav></aside>' '''.strip()
b = replace_once(b, old_sidebar, new_sidebar, 'sidebar internal links')

old_home = '''<section class="section dark"><div class="wrap">{heading('ONLINE DANIŞMANLIK SÜRECİ','Birlikte, adım adım.','Günlük hayatınızı anlayarak başlayan ve ihtiyaçlarınıza göre şekillenen bir süreç.')}{steps()}<div class="actions">{link('/online-diyetisyen/','Süreci ayrıntılı inceleyin ↗','button white')}</div></div></section>'''
new_home = '''<section class="section dark"><div class="wrap">{heading('ONLINE DANIŞMANLIK SÜRECİ','Birlikte, adım adım.','Günlük hayatınızı anlayarak başlayan ve ihtiyaçlarınıza göre şekillenen bir süreç.')}{steps()}<div class="actions">{link('/online-diyetisyen/','Süreci ayrıntılı inceleyin ↗','button white')}{link('/online-diyetisyen-fiyatlari/','2026 fiyatlarını görün ↗','button white')}{link('/sikca-sorulan-sorular/','Sık sorulan sorular ↗','button white')}</div></div></section>'''
b = replace_once(b, old_home, new_home, 'homepage journey links')

old_online_faq = '''    online+='<section class="section"><div class="wrap">'+heading('SORULARINIZ','Online görüşme hakkında')+faqs()+'</div></section>' '''.rstrip()
new_online_faq = '''    online+='<section class="section"><div class="wrap">'+heading('SORULARINIZ','Online görüşme hakkında','',('/sikca-sorulan-sorular/','Tüm sık sorulan sorular'))+faqs()+'</div></section>' '''.rstrip()
b = replace_once(b, old_online_faq, new_online_faq, 'online page FAQ link')

old_price_cta = '''    prices+='<section class="section soft"><div class="wrap price-cta"><div>'+eyebrow('BAŞLAMAYA HAZIR MISINIZ?')+'<h2>Size uygun paketi birlikte netleştirelim.</h2><p>Online görüşme süresi, takip şekli ve randevu uygunluğu için WhatsApp üzerinden bilgi alabilirsiniz.</p></div><div class="actions">'+btn(WA,'WhatsApp ile bilgi al')+btn('/online-diyetisyen/','Danışmanlık sürecini incele',True)+'</div></div></section>' '''.rstrip()
new_price_cta = '''    prices+='<section class="section soft"><div class="wrap price-cta"><div>'+eyebrow('BAŞLAMAYA HAZIR MISINIZ?')+'<h2>Size uygun paketi birlikte netleştirelim.</h2><p>Online görüşme süresi, takip şekli ve randevu uygunluğu için WhatsApp üzerinden bilgi alabilirsiniz.</p></div><div class="actions">'+btn(WA,'WhatsApp ile bilgi al')+btn('/online-diyetisyen/','Danışmanlık sürecini incele',True)+btn('/sikca-sorulan-sorular/','Sık sorulan sorular',True)+'</div></div></section>' '''.rstrip()
b = replace_once(b, old_price_cta, new_price_cta, 'price page contextual links')

old_services_body = '''        body=hero(e(s['title']),e(s['intro']),'Danışmanlık alanı')+article_body(content)'''
new_services_body = '''        body=hero(e(s['title']),e(s['intro']),'Danışmanlık alanı')+article_body(content)+'<section class="section soft"><div class="wrap"><div class="section-heading"><div>'+eyebrow('SONRAKİ ADIM')+'<h2>Online danışmanlık sürecini planlayın.</h2><p class="muted">Bu hizmet alanının online görüşmeye uygunluğu, takip biçimi ve güncel paket seçenekleri ilk iletişimde netleştirilir.</p></div></div><div class="actions">'+link('/online-diyetisyen/','Online diyetisyen süreci ↗','button')+link('/online-diyetisyen-fiyatlari/','2026 fiyatları ↗','button light')+link('/sikca-sorulan-sorular/','Sık sorulan sorular ↗','text-link')+'</div></div></section>' '''.rstrip()
b = replace_once(b, old_services_body, new_services_body, 'service page conversion links')

build.write_text(b)

# --- Expand technical SEO validation ---
c = check.read_text()
insert = r'''
# Extended technical SEO checks: exact canonicals, social metadata, sitemap completeness and orphan detection.
def page_route(file):
    rel=file.relative_to(OUT)
    if rel.as_posix()=='index.html':return '/'
    if rel.name=='index.html':return '/'+rel.parent.as_posix().strip('/')+'/'
    return '/'+rel.as_posix()

indexable={}
for file,p in pages.items():
    robots=p.meta.get('robots','') or ''
    if robots.startswith('noindex'):continue
    route=page_route(file)
    expected=BASE+route
    indexable[route]=(file,p)
    if p.canonical!=[expected]:errors.append(f'{file}: canonical must equal {expected}')
    if p.meta.get('viewport')!='width=device-width,initial-scale=1':errors.append(f'{file}: viewport')
    if robots!='index,follow,max-image-preview:large':errors.append(f'{file}: robots meta')
    for key in ['og:title','og:description','og:url','og:image']:
        if not p.meta.get(key):errors.append(f'{file}: missing {key}')
    if p.meta.get('og:url')!=expected:errors.append(f'{file}: og:url mismatch')
    if p.meta.get('og:image') and not p.meta['og:image'].startswith(BASE+'/assets/images/'):errors.append(f'{file}: og:image must be absolute')

expected_sitemap={BASE+route for route in indexable}
actual_sitemap=set(urls)
if actual_sitemap!=expected_sitemap:
    missing=sorted(expected_sitemap-actual_sitemap)
    extra=sorted(actual_sitemap-expected_sitemap)
    errors.append(f'Sitemap coverage mismatch missing={missing} extra={extra}')

incoming={route:0 for route in indexable}
for file,p in pages.items():
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc or not u.path.startswith('/'):continue
        target=unquote(u.path)
        if target in incoming:incoming[target]+=1
for route,count in incoming.items():
    if route!='/' and count==0:errors.append(f'Orphan indexable page: {route}')

robots_file=(OUT/'robots.txt').read_text()
if 'User-agent: *' not in robots_file or 'Allow: /' not in robots_file:errors.append('robots.txt basic directives')
if f'Sitemap: {BASE}/sitemap.xml' not in robots_file:errors.append('robots.txt sitemap URL')
'''
marker = "if errors:\n    print('\\n'.join(errors));raise SystemExit(1)"
if marker not in c:
    raise SystemExit('Pattern not found: check.py insertion point')
c = c.replace(marker, insert + '\n' + marker, 1)
c = c.replace("print(f'PASS: {len(pages)} HTML pages; unique titles and descriptions; Turkish language; one H1; valid JSON-LD; internal links, images and fragments; {len(urls)} sitemap URLs.')", "print(f'PASS: {len(pages)} HTML pages; metadata, exact canonicals, JSON-LD, internal links, orphan detection, robots.txt and {len(urls)} sitemap URLs validated.')", 1)
check.write_text(c)
print('Internal link network and technical SEO checks updated.')
