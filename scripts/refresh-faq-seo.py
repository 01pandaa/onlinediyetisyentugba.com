#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

FAQ_GROUPS = [
  {
    "id": "online-diyetisyen-ve-ilk-gorusme",
    "title": "Online diyetisyen ve ilk görüşme",
    "items": [
      ["Online diyetisyen nedir, nasıl çalışır?", "Online diyetisyen danışmanlığı; beslenme değerlendirmesi, kişisel planlama ve takibin uzaktan görüşmelerle yürütülmesidir. Tuğba Şeker Ağaç ile süreç günlük yaşamınızı, sağlık öykünüzü, beslenme alışkanlıklarınızı ve beklentilerinizi tanımakla başlar; görüşme kanalı ve takip kapsamı randevu öncesinde netleştirilir."],
      ["Online diyetisyen görüşmesi nasıl yapılır?", "Görüşme sesli veya görüntülü olarak planlanabilir. Görüşme öncesinde gerekli bilgiler, mevcut tetkikleriniz ve kullandığınız ilaçlar hakkında nasıl bilgi paylaşacağınız konuşulur. Online yöntem fiziksel muayenenin yerine geçmez; gerektiğinde hekim veya yüz yüze değerlendirme önerilebilir."],
      ["Türkiye’nin her ilinden online diyetisyen desteği alabilir miyim?", "Evet. Türkiye’nin farklı şehirlerinden online görüşme için iletişim kurabilirsiniz; Adana’da yaşamanız gerekmez. Online danışmanlığın sizin ihtiyaçlarınıza uygunluğu ilk iletişimde değerlendirilir. Adana’da yüz yüze görüşme seçeneği de bulunur."],
      ["Online diyetisyen güvenilir mi, nasıl seçilir?", "Diyetisyen seçerken mesleki unvanın, eğitim bilgisinin, iletişim bilgilerinin ve hizmet kapsamının açıkça paylaşılmasına dikkat edin. Kesin kilo kaybı, mucize sonuç veya herkese aynı program gibi vaatler güvenilir bir yaklaşım değildir. Sağlık durumunuzla ilgili tanı ve ilaç değişikliği için hekiminizle görüşmeniz gerekir."],
      ["Online diyetisyen ile yüz yüze diyetisyen arasındaki fark nedir?", "Temel fark görüşmenin yapıldığı ortamdır. Online süreçte değerlendirme ve takip uzaktan yürütülür; yüz yüze görüşmede ofiste buluşulur. Gerektiğinde fiziksel ölçüm veya yerinde değerlendirme ihtiyacı yöntem seçiminde dikkate alınır."],
      ["Online diyete nasıl başlarım?", "WhatsApp veya iletişim sayfası üzerinden online danışmanlık istediğinizi belirterek başlayabilirsiniz. İhtiyacınız, uygun görüşme zamanı, hizmet kapsamı ve güncel ücret bilgisi konuşulduktan sonra randevu planlanır."],
      ["İlk online diyetisyen görüşmesinde neler konuşulur?", "Sağlık öykünüz, mevcut tanılarınız, günlük öğün düzeniniz, çalışma saatleriniz, hareket düzeyiniz, sevdiğiniz ve tüketmediğiniz besinler ile hedefleriniz değerlendirilir. Amaç yalnızca ne yediğinizi değil, beslenme düzeninizin günlük hayatınızla nasıl birlikte ilerlediğini anlamaktır."],
      ["Online diyetisyen için kan tahlili gerekli mi?", "Herkes için aynı kan tahlili listesi veya zorunluluğu yoktur. Yakın tarihli mevcut sonuçlar değerlendirmeye yardımcı olabilir. Yeni tetkik gerekip gerekmediğine sağlık durumunuza göre hekim karar verir; yalnızca internette gördüğünüz bir listeye dayanarak tetkik yaptırmanız önerilmez."]
    ]
  },
  {
    "id": "beslenme-plani-ve-takip",
    "title": "Beslenme planı, takip ve günlük yaşam",
    "items": [
      ["Beslenme listesi herkese aynı mı hazırlanır?", "Hayır. Sağlık öyküsü, enerji ve besin gereksinimleri, günlük düzen, besin tercihleri, ulaşılabilir seçenekler ve kişisel hedefler birlikte değerlendirilir. Başka bir kişi için hazırlanmış bir liste sizin için uygun olmayabilir."],
      ["Kişiye özel beslenme planı ne demektir?", "Kişiye özel plan; yalnızca kalori veya porsiyon hesabı yapmak değil, sağlık bilgilerinizi, yaşam düzeninizi, çalışma saatlerinizi, yemek hazırlama olanaklarınızı ve besin tercihlerinizi birlikte değerlendirmek anlamına gelir. Plan takip görüşmelerinde ihtiyaçlara göre yeniden ele alınabilir."],
      ["Beslenme listesi ne sıklıkla değişir?", "Takip sürecinde haftalık değerlendirmelerle hangi öğünlerin uygulanabildiği ve nerede zorlanıldığı konuşulur. Liste veya alternatiflerde yapılacak değişiklikler ihtiyaca göre planlanır; her hafta değişiklik yapılması tek başına bir hedef değildir."],
      ["Online takip nasıl yapılır?", "Takipte planın günlük hayatta nasıl uygulandığı, zorlandığınız öğünler, açlık-tokluk deneyiminiz ve ihtiyaç duyduğunuz alternatifler değerlendirilir. Görüşme sıklığı ve iletişim kapsamı hizmet başlamadan önce netleştirilir."],
      ["Öğün fotoğrafları değerlendirilir mi?", "Uygun olduğunda öğün fotoğrafları günlük düzeni anlamaya yardımcı bir takip aracı olarak kullanılabilir. Fotoğraf tek başına besinin tam miktarını veya sağlık etkisini göstermez; değerlendirme görüşmedeki diğer bilgilerle birlikte yapılır."],
      ["Diyet sürecinde aç kalır mıyım, yasak besin var mı?", "Amaç sürekli aç kalmak veya uzun bir yasaklar listesi oluşturmak değildir. Herkese yönelik tek bir yasak listesi yoktur; alerji, intolerans veya tıbbi durum nedeniyle gerekli kısıtlamalar kişiye özel değerlendirilir."],
      ["Ekmek, pilav veya makarnayı tamamen bırakmalı mıyım?", "Bu besinleri herkesin tamamen bırakması gerekmez. Porsiyon, öğünün bütünü, besin çeşitliliği ve kişisel gereksinimler birlikte değerlendirilir. Tıbbi bir kısıtlamanız varsa ayrıca dikkate alınır."],
      ["Çalışırken, seyahatte veya dışarıda yemek yerken plana uyabilir miyim?", "Plan yalnızca evde yemek hazırlayabildiğiniz varsayımıyla oluşturulmaz. İş yeri yemekleri, seyahat, aile sofraları, restoran seçenekleri ve değişen çalışma saatleri görüşmede konuşularak uygulanabilir alternatifler planlanabilir."]
    ]
  },
  {
    "id": "kilo-yonetimi-ve-beklentiler",
    "title": "Kilo yönetimi ve beklentiler",
    "items": [
      ["Online diyetisyen ile kilo verilir mi?", "Online görüşme kilo yönetimi sürecinde kişisel planlama ve düzenli takip için kullanılabilir. Ancak sonuçlar kişiden kişiye değişir; yalnızca görüşmenin online olması kilo kaybı garantisi vermez. Sağlık durumu, günlük yaşam, uyku, hareket, ilaçlar ve sürdürülebilir alışkanlıklar birlikte önem taşır."],
      ["Online diyet gerçekten etkili mi?", "Uzaktan danışmanlık bazı kişiler için uygulanabilir ve sürdürülebilir bir destek seçeneğidir. Etkililik; planın kişiye uygunluğu, takip, iletişim ve değişikliklerin günlük yaşama taşınabilmesiyle ilişkilidir. Herkes için aynı sonuç veya süre vaat edilemez."],
      ["Ne kadar sürede kaç kilo veririm?", "Belirli bir sürede belirli kilo kaybı garantisi verilemez. Başlangıç ağırlığı, sağlık durumu, ilaçlar, uyku, aktivite ve günlük koşullar süreci etkileyebilir. İlerleme yalnızca tartı sayısıyla değil, sürdürülebilir alışkanlıklar ve genel süreçle birlikte değerlendirilir."],
      ["Bir öğünde plan dışına çıkarsam diyet bozulur mu?", "Tek bir öğün tüm süreci belirlemez. Planın günlük yaşama uymayan kısmını takipte paylaşmak, aşırı kısıtlayıcı telafi davranışları yerine bir sonraki öğünde olağan düzene dönmek daha uygulanabilir bir yaklaşımdır."],
      ["Tartıdaki her değişim yağ kaybı veya yağ artışı mıdır?", "Hayır. Vücut ağırlığı; yağ dokusunun yanında kas, su, glikojen ve sindirim sistemi içeriği gibi farklı bileşenlerden etkilenir. Tek bir tartım vücut yağındaki değişimi tek başına göstermez; zaman içindeki seyir ve ölçüm koşulları önemlidir."]
    ]
  },
  {
    "id": "saglik-durumlari-ve-ozel-donemler",
    "title": "Sağlık durumları ve özel dönemler",
    "items": [
      ["Diyabet veya insülin direncinde online diyetisyen desteği alınabilir mi?", "Bu durumlarda beslenme planı mevcut tanı, tedavi, ilaç kullanımı ve günlük yaşamla birlikte değerlendirilmelidir. Beslenme danışmanlığı hekim takibinin yerini almaz ve diyetisyen ilaç dozunu değiştirmez."],
      ["PCOS’ta beslenme danışmanlığı online yürütülebilir mi?", "PCOS’ta beslenme yaklaşımı kişinin sağlık bulguları, yaşam biçimi, beslenme alışkanlıkları ve varsa hekim tedavisiyle birlikte ele alınabilir. Tek bir mucize diyet veya takviye yaklaşımı yoktur; online görüşmeye uygunluk ilk değerlendirmede konuşulur."],
      ["Haşimato için online beslenme planı hazırlanabilir mi?", "Haşimato tanısı bulunan kişilerde beslenme değerlendirmesi mevcut tedavi, laboratuvar bulguları ve kişisel gereksinimlerle birlikte yapılır. Her Haşimato tanısında glutensiz beslenmenin zorunlu olduğu söylenemez; tıbbi kararlar hekiminizle birlikte ele alınmalıdır."],
      ["Gebelikte online diyetisyen desteği alınabilir mi?", "Gebelikte beslenme; gebelik haftası, başlangıç durumu, hekim takibi, laboratuvar sonuçları, besin güvenliği ve kişisel gereksinimler birlikte değerlendirilerek planlanır. Gebelikte gelişigüzel zayıflama diyeti uygulanmamalıdır."],
      ["Emzirme döneminde online beslenme danışmanlığı alınabilir mi?", "Emzirme döneminde enerji ve besin gereksinimleri, süt üretimiyle ilgili günlük düzen, uyku, sıvı alımı ve kişisel sağlık bilgileri birlikte ele alınabilir. Hızlı kilo kaybı hedefleri yerine anne ve bebeğin gereksinimlerini gözeten sürdürülebilir planlama önemlidir."],
      ["Glutensiz veya eliminasyon diyeti online yürütülebilir mi?", "Gerektiğinde bu beslenme yaklaşımları online takipte değerlendirilebilir; ancak gereksiz ve uzun süreli kısıtlamalar besin yetersizliklerine yol açabilir. Çölyak şüphesinde tanı süreci tamamlanmadan gluteni gelişigüzel kesmek testleri etkileyebileceği için hekim değerlendirmesi önemlidir."]
    ]
  },
  {
    "id": "ucret-randevu-ve-adana",
    "title": "Ücret, randevu, iletişim ve Adana",
    "items": [
      ["Online diyetisyen fiyatları neye göre değişir?", "Online diyetisyen ücretleri; görüşme ve takip kapsamı, görüşme sıklığı ve sunulan hizmetin içeriğine göre değişebilir. Sitede sabit fiyat yayınlanmadığı için güncel ücret ve kapsam bilgisini WhatsApp veya telefon üzerinden öğrenebilirsiniz."],
      ["WhatsApp üzerinden hangi saatlerde ulaşabilirim?", "WhatsApp iletişim saatleri pazartesi–cumartesi 08.00–20.00’dır; pazar günleri kapalıdır. Bu saatler anında yanıt garantisi anlamına gelmez. Acil sağlık sorunlarında mesaj yanıtı beklemek yerine uygun sağlık kuruluşuna başvurun."],
      ["Randevumu ertelemek veya iptal etmek istersem ne yapmalıyım?", "Değişiklik ihtiyacınızı mümkün olduğunca erken telefon veya WhatsApp üzerinden iletebilirsiniz. Erteleme, iptal ve varsa ödeme koşullarını hizmet başlamadan önce doğrudan teyit etmeniz en doğru yaklaşımdır."],
      ["Adana’da yüz yüze diyetisyen görüşmesi yapıyor musunuz?", "Evet. Online danışmanlığa ek olarak Adana Seyhan’daki ofiste randevulu yüz yüze görüşme seçeneği bulunur. Gelmeden önce randevu saatini ve adres bilgisini teyit edebilirsiniz."],
      ["Adana’daki diyetisyen ofisi nerede?", "Ofis Kurtuluş Mahallesi, Demokrasi Sokak, Atatürk Caddesi, Gülbahçesi Sitesi B/Blok Kat:2 No:205, Seyhan / Adana adresindedir. İletişim sayfasındaki harita bağlantısından konumu açabilirsiniz."],
      ["Sağlık bilgilerimi bu siteye girmeli miyim?", "Sitede doğrudan sağlık bilgisi toplayan bir form bulunmaz. BKİ aracındaki bilgiler sunucuya gönderilmez. Tetkik ve diğer hassas sağlık bilgilerinizi paylaşmadan önce danışmanlık sürecindeki güvenli paylaşım yöntemini doğrudan görüşün."]
    ]
  }
]

faq_path = ROOT / "content" / "faq.json"
faq_path.write_text(json.dumps(FAQ_GROUPS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

site_path = ROOT / "content" / "site.json"
site = json.loads(site_path.read_text(encoding="utf-8"))
site["updated"] = "2026-09-09"
site.setdefault("page_updates", {})["/sikca-sorulan-sorular/"] = "2026-09-09"
site_path.write_text(json.dumps(site, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

build_path = ROOT / "scripts" / "build.py"
build = build_path.read_text(encoding="utf-8")
start = build.index("    faq_body=hero(")
end = build.index("\n\n    online=hero(", start)
new_block = r'''    faq_count=sum(len(group['items']) for group in FAQ_GROUPS)
    faq_body=hero('Online Diyetisyen Hakkında<br><span class="accent">Sıkça Sorulan Sorular.</span>','Online diyetisyen nasıl çalışır, ilk görüşmede ne olur, kan tahlili gerekir mi, takip nasıl yürür ve ücretler neye göre değişir? En çok merak edilen konuları açık ve anlaşılır şekilde yanıtladım.','Online Diyetisyen · SSS')
    faq_body+='<section class="section faq-page"><div class="wrap">'
    faq_body+='<div class="faq-intro-card">'+eyebrow('HIZLI REHBER')+'<h2>Aradığınız yanıtı konu başlığına göre bulun.</h2><p>Bu sayfa, online beslenme danışmanlığına başlamadan önce en sık sorulan soruları bir araya getirir. Sürecin ayrıntıları için '+link('/online-diyetisyen/','online diyetisyen danışmanlığı')+', çalışma alanları için '+link('/hizmetler/','hizmetler')+' ve yüz yüze görüşmeler için '+link('/adana-diyetisyen/','Adana diyetisyen')+' sayfasını inceleyebilirsiniz.</p><nav class="faq-topic-nav" aria-label="Sıkça sorulan sorular konu başlıkları">'+''.join('<a href="#'+e(group['id'])+'">'+e(group['title'])+'</a>' for group in FAQ_GROUPS)+'</nav></div>'
    for group in FAQ_GROUPS:
        faq_body+='<section class="faq-category" id="'+e(group['id'])+'"><div class="faq-category-head"><span class="faq-category-count">'+str(len(group['items']))+' soru</span><h2>'+e(group['title'])+'</h2></div>'+faqs(group['items'])+'</section>'
    faq_body+='<section class="faq-seo-links"><div>'+eyebrow('İLGİLİ REHBERLER')+'<h2>Online diyetisyen sürecini daha ayrıntılı inceleyin.</h2><p>SSS yanıtlarından sonra ihtiyacınıza uygun rehbere geçebilirsiniz.</p></div><div class="faq-link-grid">'+link('/online-diyetisyen/','<strong>Online diyetisyen nasıl çalışır?</strong><span>Görüşme, planlama ve takip sürecini adım adım inceleyin. →</span>','faq-link-card')+link('/blog/online-diyetisyen-nasil-secilir/','<strong>Online diyetisyen nasıl seçilir?</strong><span>Uzmanlık, güven ve hizmet kapsamını değerlendirirken nelere bakılmalı? →</span>','faq-link-card')+link('/blog/online-diyetisyen-sureci/','<strong>Online diyetisyen süreci</strong><span>İlk iletişimden takip görüşmelerine kadar ayrıntılı rehber. →</span>','faq-link-card')+link('/adana-diyetisyen/','<strong>Adana’da yüz yüze görüşme</strong><span>Seyhan’daki ofis, iletişim ve randevu bilgileri. →</span>','faq-link-card')+'</div></section>'
    faq_body+='<div class="faq-help"><h2>Aradığınız soruyu bulamadınız mı?</h2><p>Kendi koşullarınızı ve size uygun görüşme yöntemini doğrudan konuşabiliriz.</p><div class="actions">'+btn(WA,'WhatsApp ile sorun')+btn('/iletisim/','İletişim bilgileri',True)+'</div></div>'
    faq_body+='<div class="faq-sources"><h2>İçerik kapsamı</h2><p>Bu yanıtlar genel bilgilendirme amaçlıdır; kişisel tanı, tedavi veya beslenme planı yerine geçmez. Sağlık durumuna özel içeriklerde güncel bilimsel rehberler ve resmi sağlık kaynakları esas alınır.</p><p>'+link('/kaynaklar/','Kaynaklar ve içerik ilkelerini inceleyin ↗','text-link')+' · '+link('/blog/','Beslenme bloguna geçin ↗','text-link')+'</p></div></div></section>'
    layout('/sikca-sorulan-sorular/','Online Diyetisyen SSS: Süreç, Fiyat ve Takip | Tuğba Şeker Ağaç',f'Online diyetisyen nasıl çalışır? İlk görüşme, kan tahlili, kişisel beslenme planı, takip, fiyat ve Adana randevusu hakkında {faq_count} sık soruya yanıt.',faq_body)'''
build = build[:start] + new_block + build[end:]
build = build.replace("?v=services-seo-v5", "?v=faq-seo-v1")
build_path.write_text(build, encoding="utf-8")

style_path = ROOT / "assets" / "style.css"
style = style_path.read_text(encoding="utf-8")
marker = "/* FAQ SEO refresh 2026-09-09 */"
if marker in style:
    style = style.split(marker)[0].rstrip() + "\n"
style += r'''

/* FAQ SEO refresh 2026-09-09 */
.faq-page{background:linear-gradient(180deg,#fbfaf5 0%,#fff 28%,#f8faf6 100%)}
.faq-intro-card{margin-bottom:42px;padding:34px 36px;border:1px solid #dbe5d9;border-radius:28px;background:linear-gradient(135deg,#f6f1e4,#eef6e9);box-shadow:0 18px 45px rgba(24,57,46,.07)}
.faq-intro-card h2{max-width:760px;margin:8px 0 12px;color:#173d31;font-size:clamp(28px,3vw,42px)}
.faq-intro-card p{max-width:920px;margin:0;color:#4c625a;line-height:1.75}
.faq-intro-card p a{font-weight:750;color:#246b45;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
.faq-topic-nav{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.faq-topic-nav a{display:inline-flex;align-items:center;min-height:42px;padding:9px 14px;border:1px solid #cfdccd;border-radius:999px;background:rgba(255,255,255,.82);color:#24523f;font-size:14px;font-weight:750;text-decoration:none;transition:transform .2s ease,border-color .2s ease,background .2s ease}
.faq-topic-nav a:hover{transform:translateY(-1px);border-color:#8db79a;background:#fff}
.faq-category{scroll-margin-top:120px;margin:0 0 38px;padding:30px;border:1px solid #e0e8df;border-radius:26px;background:#fff;box-shadow:0 12px 32px rgba(24,57,46,.05)}
.faq-category-head{display:flex;align-items:flex-end;justify-content:space-between;gap:18px;margin-bottom:18px}
.faq-category-head h2{margin:0;color:#173d31;font-size:clamp(25px,2.5vw,34px)}
.faq-category-count{flex:0 0 auto;padding:7px 11px;border-radius:999px;background:#eef6e9;color:#39704b;font-size:12px;font-weight:800;letter-spacing:.04em;text-transform:uppercase}
.faq-category .faq{display:grid;gap:10px}
.faq-category .faq details{border:1px solid #e3e9e2;border-radius:16px;background:#fcfdfb;overflow:hidden}
.faq-category .faq summary{padding:18px 20px;color:#1f4738;font-weight:780;line-height:1.45;cursor:pointer}
.faq-category .faq details[open]{border-color:#bcd0bd;background:#fff}
.faq-category .faq details p{margin:0;padding:0 20px 20px;color:#52655e;line-height:1.75}
.faq-seo-links{display:grid;grid-template-columns:minmax(0,.75fr) minmax(0,1.25fr);gap:32px;margin:50px 0;padding:36px;border-radius:28px;background:#173d31;color:#fff}
.faq-seo-links h2{margin:8px 0 12px;color:#fff;font-size:clamp(28px,3vw,40px)}
.faq-seo-links p{color:#dbe7df;line-height:1.7}
.faq-seo-links .eyebrow{color:#bfe0c4}
.faq-link-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.faq-link-card{display:flex;flex-direction:column;gap:7px;min-height:132px;padding:19px;border:1px solid rgba(255,255,255,.14);border-radius:18px;background:rgba(255,255,255,.08);color:#fff;text-decoration:none;transition:transform .2s ease,background .2s ease}
.faq-link-card:hover{transform:translateY(-2px);background:rgba(255,255,255,.13)}
.faq-link-card strong{font-size:17px;line-height:1.35}
.faq-link-card span{color:#d7e5dc;font-size:14px;line-height:1.55}
.faq-help{margin-top:34px}
@media (max-width:820px){.faq-intro-card,.faq-category,.faq-seo-links{padding:24px}.faq-seo-links{grid-template-columns:1fr}.faq-link-grid{grid-template-columns:1fr}.faq-category-head{align-items:flex-start;flex-direction:column-reverse;gap:8px}}
'''
style_path.write_text(style, encoding="utf-8")

print(f"FAQ SEO refresh prepared: {sum(len(g['items']) for g in FAQ_GROUPS)} questions")
