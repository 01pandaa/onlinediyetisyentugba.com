#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
build_path = ROOT / 'scripts' / 'build.py'
css_path = ROOT / 'assets' / 'style.css'

build = build_path.read_text()

old_online = """    online+=article_body(content)+'<section class=\"section soft\"><div class=\"wrap\">'+heading('DANIŞMANLIK ALANLARI','Hangi konuda birlikte çalışabiliriz?')+cards()+'</div></section><section class=\"section\"><div class=\"wrap\">'+heading('SORULARINIZ','Online görüşme hakkında')+faqs()+'</div></section>'\n    layout('/online-diyetisyen/','Online Diyetisyen | Türkiye Genelinde Tuğba Şeker Ağaç','Online diyetisyen danışmanlığı nasıl işler? İlk görüşme, kişisel beslenme planı, haftalık takip ve Türkiye genelinden katılım bilgileri.',online,cover='online-diyetisyen-kapak.webp')\n"""

new_online = """    online+=article_body(content)+'<section class=\"section soft\"><div class=\"wrap\">'+heading('DANIŞMANLIK ALANLARI','Hangi konuda birlikte çalışabiliriz?')+cards()+'</div></section>'\n    online+='<section class=\"section price-preview\"><div class=\"wrap price-preview-inner\"><div>'+eyebrow('2026 ONLINE PAKETLER')+'<h2>Online diyetisyen fiyatlarını inceleyin.</h2><p>1, 3 ve 6 aylık online danışmanlık paketlerinin güncel ücretlerini ve paket seçerken bilmeniz gerekenleri ayrı sayfada bulabilirsiniz.</p></div>'+link('/online-diyetisyen-fiyatlari/','Güncel fiyatları gör <span aria-hidden=\"true\">→</span>','button')+'</div></section>'\n    online+='<section class=\"section\"><div class=\"wrap\">'+heading('SORULARINIZ','Online görüşme hakkında')+faqs()+'</div></section>'\n    layout('/online-diyetisyen/','Online Diyetisyen | Türkiye Genelinde Tuğba Şeker Ağaç','Online diyetisyen danışmanlığı nasıl işler? İlk görüşme, kişisel beslenme planı, haftalık takip ve Türkiye genelinden katılım bilgileri.',online,cover='online-diyetisyen-kapak.webp')\n\n    price_schema={'@type':'Service','name':'Online Diyetisyen Danışmanlığı','provider':{'@id':BASE+'/#kurum'},'areaServed':{'@type':'Country','name':'Türkiye'},'url':BASE+'/online-diyetisyen-fiyatlari/','serviceType':'Online beslenme danışmanlığı','offers':[\n        {'@type':'Offer','name':'1 Aylık Online Paket','price':'3000','priceCurrency':'TRY','url':BASE+'/online-diyetisyen-fiyatlari/'},\n        {'@type':'Offer','name':'3 Aylık Online Paket','price':'8000','priceCurrency':'TRY','url':BASE+'/online-diyetisyen-fiyatlari/'},\n        {'@type':'Offer','name':'6 Aylık Online Paket','price':'15000','priceCurrency':'TRY','url':BASE+'/online-diyetisyen-fiyatlari/'}\n    ]}\n    prices=hero('Online Diyetisyen<br><span class=\"accent\">Fiyatları 2026.</span>','Diyetisyen Tuğba Şeker Ağaç ile online beslenme danışmanlığı için 1, 3 ve 6 aylık güncel paket seçeneklerini inceleyin.','Online diyetisyen fiyatları · 2026')\n    prices+='<section class=\"section price-page\"><div class=\"wrap\"><div class=\"price-page-heading\">'+eyebrow('GÜNCEL ONLINE PAKETLER')+'<h2>Size uygun takip süresini seçin.</h2><p>Bu sayfadaki ücretler Diyetisyen Tuğba Şeker Ağaç’ın online danışmanlık paketlerine aittir. Paket kapsamı, görüşme düzeni ve başlangıç tarihi randevu öncesinde netleştirilir.</p></div><div class=\"price-grid\"><article class=\"price-card\"><span class=\"price-term\">1 AYLIK ONLINE PAKET</span><strong class=\"price-amount\">3.000 TL</strong><p>Online beslenme danışmanlığına başlamak ve süreci kısa bir dönem boyunca takip etmek isteyenler için.</p>'+btn(WA,'Paket hakkında bilgi al')+'</article><article class=\"price-card featured\"><span class=\"price-badge\">EN ÇOK TERCİH EDİLEN</span><span class=\"price-term\">3 AYLIK ONLINE PAKET</span><strong class=\"price-amount\">8.000 TL</strong><p>Beslenme düzenini birkaç ay boyunca takip etmek ve değişen ihtiyaçları görüşmelerde değerlendirmek isteyenler için.</p>'+btn(WA,'Paket hakkında bilgi al')+'</article><article class=\"price-card\"><span class=\"price-term\">6 AYLIK ONLINE PAKET</span><strong class=\"price-amount\">15.000 TL</strong><p>Daha uzun süreli takip planlayan ve beslenme alışkanlıklarını zamana yayarak değerlendirmek isteyenler için.</p>'+btn(WA,'Paket hakkında bilgi al')+'</article></div><p class=\"price-update-note\">Fiyat güncelleme tarihi: 9 Eylül 2026. Güncel randevu ve paket kapsamı için iletişime geçebilirsiniz.</p></div></section>'\n    prices+=article_body('<h2>Online diyetisyen fiyatları neye göre değişir?</h2><p>Online danışmanlık ücretleri takip süresine, görüşme sıklığına ve sunulan hizmet kapsamına göre farklılaşabilir. Buradaki 1, 3 ve 6 aylık paketler Tuğba Şeker Ağaç’ın güncel online danışmanlık seçenekleridir.</p><h2>Paketin içinde neler konuşulur?</h2><p>Süreç; sağlık öyküsü, günlük öğün düzeni, çalışma saatleri, besin tercihleri ve hedeflerin değerlendirilmesiyle başlar. Kişisel beslenme planı ve takip yapısı görüşme sırasında ihtiyaçlarınıza göre ele alınır. İlaç düzenleme veya tıbbi tanı diyetisyen hizmetinin kapsamında değildir.</p><h2>Hangi online diyetisyen paketini seçmeliyim?</h2><p>Tek bir paket herkes için en doğru seçenek değildir. Takip etmek istediğiniz süre, mevcut sağlık durumunuz, günlük yaşamınız ve beklentileriniz değerlendirilerek uygun süre birlikte konuşulabilir. Karar vermeden önce <a href=\"/online-diyetisyen/\">online diyetisyen sürecini</a> inceleyebilirsiniz.</p><h2>Online danışmanlığa nasıl başlarım?</h2><p>WhatsApp üzerinden iletişime geçerek online danışmanlık istediğinizi belirtebilirsiniz. Uygun görüşme zamanı, seçilen paket ve hizmet kapsamı netleştirildikten sonra randevu planlanır. WhatsApp iletişim saatleri pazartesi–cumartesi 08.00–20.00’dır; pazar günleri kapalıdır.</p><h2>Online diyetisyen fiyatı ile yüz yüze görüşme ücreti aynı mı?</h2><p>Bu sayfadaki ücretler yalnızca online danışmanlık paketlerine aittir. Adana Seyhan’daki yüz yüze görüşmelerin güncel ücret bilgisi için <a href=\"/iletisim/\">iletişim sayfasından</a> bilgi alabilirsiniz.</p>')\n    prices+='<section class=\"section soft\"><div class=\"wrap price-cta\"><div>'+eyebrow('BAŞLAMAYA HAZIR MISINIZ?')+'<h2>Size uygun paketi birlikte netleştirelim.</h2><p>Online görüşme süresi, takip şekli ve randevu uygunluğu için WhatsApp üzerinden bilgi alabilirsiniz.</p></div><div class=\"actions\">'+btn(WA,'WhatsApp ile bilgi al')+btn('/online-diyetisyen/','Danışmanlık sürecini incele',True)+'</div></div></section>'\n    layout('/online-diyetisyen-fiyatlari/','Online Diyetisyen Fiyatları 2026 | Tuğba Şeker Ağaç','Online diyetisyen fiyatları 2026: 1 aylık 3.000 TL, 3 aylık 8.000 TL, 6 aylık 15.000 TL. Tuğba Şeker Ağaç online danışmanlık paketleri.',prices,extra=[price_schema],cover='online-diyetisyen-kapak.webp')\n"""

if old_online not in build:
    raise SystemExit('Online page insertion marker not found')
build = build.replace(old_online, new_online, 1)

old_links = """+link('/blog/online-diyetisyen-sureci/','<strong>Online diyetisyen süreci</strong><span>İlk iletişimden takip görüşmelerine kadar ayrıntılı rehber. →</span>','faq-link-card')+link('/adana-diyetisyen/','<strong>Adana’da yüz yüze görüşme</strong><span>Seyhan’daki ofis, iletişim ve randevu bilgileri. →</span>','faq-link-card')"""
new_links = """+link('/blog/online-diyetisyen-sureci/','<strong>Online diyetisyen süreci</strong><span>İlk iletişimden takip görüşmelerine kadar ayrıntılı rehber. →</span>','faq-link-card')+link('/online-diyetisyen-fiyatlari/','<strong>Online diyetisyen fiyatları 2026</strong><span>1, 3 ve 6 aylık güncel online paketleri karşılaştırın. →</span>','faq-link-card')+link('/adana-diyetisyen/','<strong>Adana’da yüz yüze görüşme</strong><span>Seyhan’daki ofis, iletişim ve randevu bilgileri. →</span>','faq-link-card')"""
if old_links not in build:
    raise SystemExit('FAQ related-links marker not found')
build = build.replace(old_links, new_links, 1)

build = build.replace('?v=faq-seo-v1', '?v=prices-v1')
build_path.write_text(build)

css = css_path.read_text()
marker = '/* online-price-page-v1 */'
if marker not in css:
    css += r'''

/* online-price-page-v1 */
.price-preview{padding-top:0}
.price-preview-inner{display:flex;align-items:center;justify-content:space-between;gap:32px;padding:30px 34px;border:1px solid rgba(22,78,51,.14);border-radius:28px;background:linear-gradient(135deg,#f7f1e5,#eef7f0)}
.price-preview-inner h2{margin:8px 0 10px}
.price-preview-inner p{margin:0;max-width:720px}
.price-page-heading{max-width:780px;margin-bottom:34px}
.price-page-heading h2{margin:8px 0 12px}
.price-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;align-items:stretch}
.price-card{position:relative;display:flex;flex-direction:column;gap:16px;min-height:360px;padding:34px;border:1px solid rgba(22,78,51,.15);border-radius:28px;background:#fff;box-shadow:0 18px 45px rgba(22,78,51,.07)}
.price-card.featured{border:2px solid #237a50;transform:translateY(-8px);box-shadow:0 24px 55px rgba(22,78,51,.13)}
.price-badge{align-self:flex-start;margin-top:-50px;margin-bottom:4px;padding:8px 14px;border-radius:999px;background:#164e33;color:#fff;font-size:.75rem;font-weight:800;letter-spacing:.08em}
.price-term{color:#164e33;font-size:.86rem;font-weight:800;letter-spacing:.07em}
.price-amount{display:block;color:#237a50;font-size:clamp(2.1rem,4vw,3.4rem);line-height:1;font-weight:800}
.price-card p{flex:1;margin:0;color:#607066;line-height:1.7}
.price-card .button{align-self:flex-start}
.price-update-note{margin:26px 0 0;text-align:center;color:#66756c;font-size:.92rem}
.price-cta{display:flex;align-items:center;justify-content:space-between;gap:36px}
.price-cta h2{margin:8px 0 10px}
.price-cta p{margin:0;max-width:700px}
@media (max-width:900px){.price-grid{grid-template-columns:1fr}.price-card.featured{transform:none;margin-top:12px}.price-preview-inner,.price-cta{align-items:flex-start;flex-direction:column}.price-card{min-height:0}}
@media (max-width:560px){.price-card,.price-preview-inner{padding:26px 22px;border-radius:22px}.price-badge{margin-top:-42px}.price-amount{font-size:2.45rem}}
'''
    css_path.write_text(css)

print('Added /online-diyetisyen-fiyatlari/ with 2026 online package pricing and internal links.')
