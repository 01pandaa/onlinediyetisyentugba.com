#!/usr/bin/env python3
"""Strengthen /online-diyetisyen/ as the primary generic search-intent pillar."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'scripts' / 'build.py'
SITE = ROOT / 'content' / 'site.json'


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'Pattern not found: {label}')
    return text.replace(old, new, 1)

b = BUILD.read_text()

b = replace_once(
    b,
    "<div class=\"wrap\"><p>İyi beslenmek, hayatın içinde sürdürebildiğin bir dengeyle başlar.</p>{link('/vucudunu-tani/','Beslenmenin bilimini keşfet ↗','text-link')}</div></div>",
    "<div class=\"wrap\"><p>İyi beslenmek, hayatın içinde sürdürebildiğin bir dengeyle başlar.</p><div class=\"actions\">{link('/online-diyetisyen/','Online diyetisyen nasıl çalışır? ↗','text-link')}{link('/vucudunu-tani/','Beslenmenin bilimini keşfet ↗','text-link')}</div></div></div>",
    'homepage primary online link'
)

b = replace_once(
    b,
    "{link('/online-diyetisyen/','Süreci ayrıntılı inceleyin ↗','button white')}",
    "{link('/online-diyetisyen/','Online diyetisyen sürecini inceleyin ↗','button white')}",
    'homepage online CTA anchor'
)

b = replace_once(
    b,
    "layout('/','Online Diyetisyen Tuğba Şeker Ağaç | Türkiye & Adana','Türkiye genelinde online diyetisyen Tuğba Şeker Ağaç ile kişisel beslenme danışmanlığı. Kilo yönetimi, kaynaklı beslenme rehberleri ve Adana ofisi.',body)",
    "layout('/','Diyetisyen Tuğba Şeker Ağaç | Online & Adana','Diyetisyen Tuğba Şeker Ağaç; Türkiye genelinde online beslenme danışmanlığı ve Adana’da yüz yüze görüşme sunar. Hizmetler, blog ve iletişim bilgileri.',body)",
    'homepage title intent separation'
)

old_online = """    online=hero('Türkiye genelinde<br><span class=\"accent\">online diyetisyen danışmanlığı.</span>','Bulunduğunuz şehirden, kendi yaşam düzeniniz içinden beslenme görüşmelerine katılın. Süreci, kapsamını ve takip adımlarını bu sayfada öğrenin.','Online danışmanlık','online-diyetisyen-kapak.webp','wide-cover','Diyetisyen Tuğba Şeker Ağaç markasına ait online beslenme danışmanlığı kapak görseli')
    online+='<section class=\"section dark\"><div class=\"wrap\">'+heading('NASIL İLERLİYORUZ?','Hayatınızı tanıyan bir süreç.')+steps()+'</div></section>'
    content=''.join(f'<section id=\"{e(s[\"id\"])}\"><h2>{e(s[\"title\"])}</h2>{s[\"body\"]}</section>' for s in ONLINE['sections'])
    online+=article_body(content)+'<section class=\"section soft\"><div class=\"wrap\">'+heading('DANIŞMANLIK ALANLARI','Hangi konuda birlikte çalışabiliriz?')+cards()+'</div></section>'
    online+='<section class=\"section price-preview\"><div class=\"wrap price-preview-inner\"><div>'+eyebrow('2026 ONLINE PAKETLER')+'<h2>Online diyetisyen fiyatlarını inceleyin.</h2><p>1, 3 ve 6 aylık online danışmanlık paketlerinin güncel ücretlerini ve paket seçerken bilmeniz gerekenleri ayrı sayfada bulabilirsiniz.</p></div>'+link('/online-diyetisyen-fiyatlari/','Güncel fiyatları gör <span aria-hidden=\"true\">→</span>','button')+'</div></section>'
    online+='<section class=\"section\"><div class=\"wrap\">'+heading('SORULARINIZ','Online görüşme hakkında','',('/sikca-sorulan-sorular/','Tüm sık sorulan sorular'))+faqs()+'</div></section>'
    layout('/online-diyetisyen/','Online Diyetisyen | Türkiye Genelinde Tuğba Şeker Ağaç','Online diyetisyen danışmanlığı nasıl işler? İlk görüşme, kişisel beslenme planı, haftalık takip ve Türkiye genelinden katılım bilgileri.',online,cover='online-diyetisyen-kapak.webp')
"""

new_online = """    online_schema={'@type':'Service','@id':BASE+'/online-diyetisyen/#service','name':'Online Diyetisyen Danışmanlığı','serviceType':'Online beslenme danışmanlığı','provider':{'@id':BASE+'/#kurum'},'areaServed':{'@type':'Country','name':'Türkiye'},'url':BASE+'/online-diyetisyen/'}
    online=hero('Online diyetisyen ile<br><span class=\"accent\">Türkiye genelinde kişiye özel beslenme danışmanlığı.</span>','Diyetisyen Tuğba Şeker Ağaç ile bulunduğunuz şehirden online görüşmeye katılın. İlk görüşme, kişisel beslenme planı, düzenli takip, ücretler ve online diyetisyen seçimi hakkında merak ettiklerinizi bu rehberde bulabilirsiniz.','Online Diyetisyen','online-diyetisyen-kapak.webp','wide-cover','Diyetisyen Tuğba Şeker Ağaç markasına ait online beslenme danışmanlığı kapak görseli')
    online+='<section class=\"section online-hub-intro\"><div class=\"wrap\"><div class=\"faq-intro-card\">'+eyebrow('ONLINE DİYETİSYEN REHBERİ')+'<h2>Online danışmanlık hakkında aradığınız bilgiye hızlıca ulaşın.</h2><p>Bu sayfa, <strong>online diyetisyen</strong> hizmetinin nasıl çalıştığını tek yerde açıklayan ana rehberdir. Süreci öğrenebilir, görüşmeye hazırlanabilir, takip biçimini inceleyebilir ve güncel paketlere geçebilirsiniz.</p><nav class=\"faq-topic-nav\" aria-label=\"Online diyetisyen rehberi konu başlıkları\">'+link('#online-diyetisyen-nedir','Online diyetisyen nedir?')+link('#online-diyetisyen-nasil-calisir','Nasıl çalışır?')+link('#ilk-gorusme','İlk görüşme')+link('#takip','Takip')+link('#online-diyetisyen-nasil-secilir','Nasıl seçilir?')+link('#baslangic-ve-ucret','Fiyat ve başlangıç')+'</nav></div></div></section>'
    online+='<section class=\"section dark\"><div class=\"wrap\">'+heading('ONLINE DANIŞMANLIK SÜRECİ','Online diyetisyen ile nasıl ilerliyoruz?','İlk değerlendirmeden takibe kadar her adım kişisel ihtiyaçlarınıza ve günlük yaşamınıza göre ele alınır.')+steps()+'</div></section>'
    content=''.join(f'<section id=\"{e(s[\"id\"])}\"><h2>{e(s[\"title\"])}</h2>{s[\"body\"]}</section>' for s in ONLINE['sections'])
    online+=article_body(content)+'<section class=\"section soft\"><div class=\"wrap\">'+heading('DANIŞMANLIK ALANLARI','Online diyetisyen hangi konularda destek olabilir?','Kilo yönetiminden farklı yaşam dönemlerine kadar çalışma alanlarını inceleyin.')+cards()+'</div></section>'
    online+='<section class=\"section price-preview\"><div class=\"wrap price-preview-inner\"><div>'+eyebrow('2026 ONLINE PAKETLER')+'<h2>Online diyetisyen fiyatlarını inceleyin.</h2><p>1, 3 ve 6 aylık online danışmanlık paketlerinin güncel ücretlerini, kapsam bilgisini ve paket seçerken bilmeniz gerekenleri ayrı sayfada bulabilirsiniz.</p></div>'+link('/online-diyetisyen-fiyatlari/','Online diyetisyen fiyatları 2026 <span aria-hidden=\"true\">→</span>','button')+'</div></section>'
    online+='<section class=\"section\"><div class=\"wrap\">'+heading('SORULARINIZ','Online diyetisyen hakkında sık sorulan sorular','',('/sikca-sorulan-sorular/','Tüm online diyetisyen soruları'))+faqs()+'</div></section>'
    online+='<section class=\"section soft\"><div class=\"wrap price-cta\"><div>'+eyebrow('ONLINE DANIŞMANLIĞA BAŞLANGIÇ')+'<h2>Online diyetisyen görüşmesine başlamak ister misiniz?</h2><p>Görüşme yöntemi, size uygun takip süresi ve randevu bilgilerini WhatsApp üzerinden konuşabilir; önce <a href=\"/online-diyetisyen-fiyatlari/\">2026 online paketlerini</a> veya <a href=\"/sikca-sorulan-sorular/\">sık sorulan soruları</a> inceleyebilirsiniz.</p></div><div class=\"actions\">'+btn(WA,'Online görüşme bilgisi al')+btn('/online-diyetisyen-fiyatlari/','Fiyatları incele',True)+btn('/hizmetler/','Hizmetleri incele',True)+'</div></div></section>'
    layout('/online-diyetisyen/','Online Diyetisyen | Tuğba Şeker Ağaç – Türkiye Geneli','Online diyetisyen Tuğba Şeker Ağaç ile Türkiye genelinde kişiye özel beslenme danışmanlığı. İlk görüşme, takip, süreç ve 2026 fiyat bilgileri.',online,extra=[online_schema],cover='online-diyetisyen-kapak.webp')
"""

b = replace_once(b, old_online, new_online, 'online pillar block')
BUILD.write_text(b)

site = json.loads(SITE.read_text())
site['updated'] = '2026-09-10'
site.setdefault('page_updates', {})['/'] = '2026-09-10'
site['page_updates']['/online-diyetisyen/'] = '2026-09-10'
SITE.write_text(json.dumps(site, ensure_ascii=False, indent=2) + '\n')

print('Online dietitian pillar strengthened and homepage intent separated.')
