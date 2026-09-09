#!/usr/bin/env python3
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
services_path=ROOT/'content/services.json'
build_path=ROOT/'scripts/build.py'
css_path=ROOT/'assets/style.css'
site_path=ROOT/'content/site.json'

new_services=[
  {
    "slug":"insulin-direncinde-beslenme",
    "title":"İnsülin Direncinde Beslenme",
    "seo_title":"İnsülin Direncinde Beslenme | Online Diyetisyen",
    "meta_description":"İnsülin direncinde beslenme nasıl planlanır? Öğün düzeni, karbonhidrat kalitesi, lif-protein dengesi ve sürdürülebilir kilo yönetimi hakkında online diyetisyen desteği.",
    "short":"İnsülin direncinde öğün düzeni, besin seçimi ve yaşam tarzı alışkanlıklarını birlikte değerlendiren kişisel beslenme danışmanlığı.",
    "intro":"İnsülin direncinde tek bir yasak listesi yerine; günlük öğün düzeni, karbonhidrat kaynakları, lif ve protein dengesi, hareket, uyku ve varsa hekim tedavisi birlikte değerlendirilir. Amaç uygulanabilir ve sürdürülebilir bir beslenme düzeni oluşturmaktır.",
    "sections":[
      ["İnsülin direncinde beslenme yaklaşımı", "<p>İnsülin direnci bulunan kişilerde beslenme planı kişisel sağlık öyküsü, günlük yaşam ve varsa ilaç tedavisi dikkate alınarak hazırlanır. Herkese aynı öğün sayısı veya aynı karbonhidrat miktarı önerilmez.</p><p>Öğünlerde sebze, tam tahıl, baklagil ve diğer lif kaynakları ile uygun protein kaynaklarının dengelenmesi; rafine karbonhidratların sıklığının ve porsiyonlarının kişiye göre değerlendirilmesi sürecin parçasıdır.</p>"],
      ["Kilo yönetimi ve günlük düzen", "<p>Kilo kaybı gerekiyorsa hedef hızlı sonuç değil, sürdürülebilir ilerlemedir. İş saatleri, dışarıda yeme, uyku ve fiziksel aktivite planın uygulanabilirliğini etkiler.</p><ul><li>Öğün atlama ve uzun açlık dönemlerinin değerlendirilmesi.</li><li>Pratik ara öğün gereksiniminin kişiye göre belirlenmesi.</li><li>Ev ve iş ortamına uygun alternatifler.</li></ul>"],
      ["Takipte neleri değerlendiriyoruz?", "<p>Açlık-tokluk durumu, öğünlerin uygulanabilirliği, enerji düzeyi ve varsa hekim tarafından izlenen laboratuvar sonuçları birlikte ele alınabilir. İlaç dozları diyetisyen tarafından değiştirilmez.</p>"],
      ["Online diyetisyen desteği", "<p>Online görüşmelerde günlük rutininize göre plan hazırlanır ve takipte uygulanamayan noktalar yeniden düzenlenir. Amaç kısa süreli bir liste değil, günlük hayata uyarlanabilen bir sistem oluşturmaktır.</p>"]
    ],
    "related":"insulin-direncinde-beslenme",
    "source":"https://www.niddk.nih.gov/health-information/diabetes/overview/what-is-diabetes/prediabetes-insulin-resistance"
  },
  {
    "slug":"hasimato-diyeti",
    "title":"Haşimato Diyeti ve Beslenme",
    "seo_title":"Haşimato Diyeti ve Beslenme | Online Diyetisyen",
    "meta_description":"Haşimato tiroiditinde beslenme; tiroid tedavisi, öğün düzeni, besin çeşitliliği ve kişisel gereksinimlerle birlikte ele alınır. Online diyetisyen desteği.",
    "short":"Haşimato ve tiroid hastalıklarında hekim tedavisiyle uyumlu, kişiye göre planlanan beslenme danışmanlığı.",
    "intro":"Haşimato için herkese uyan tek bir diyet yoktur. Beslenme yaklaşımı tiroid fonksiyonları, hekim tedavisi, mevcut tetkikler, günlük yaşam, besin toleransı ve kişisel hedefler birlikte değerlendirilerek planlanır.",
    "sections":[
      ["Haşimato için tek bir özel diyet var mı?", "<p>Haşimato tiroiditini tek başına iyileştirdiği kanıtlanmış belirli bir besin veya standart bir diyet bulunmaz. Gereksiz kısıtlamalar yerine yeterli ve dengeli beslenme, kişisel gereksinimler ve tıbbi takip esas alınır.</p>"],
      ["Gluten, süt ürünleri ve eliminasyon", "<p>Çölyak hastalığı, alerji veya başka bir tıbbi gerekçe yoksa besin gruplarını otomatik olarak çıkarmak uygun değildir. Eliminasyon gerekiyorsa süre, kapsam ve yeniden deneme adımları planlı biçimde yürütülür.</p>"],
      ["Tiroid ilacı ve öğün düzeni", "<p>Kullanılan tiroid ilacının zamanlaması ve hekim önerileri beslenme görüşmesinde dikkate alınır. İlaç dozuna müdahale edilmez. Demir, kalsiyum veya başka takviyeler kullanılıyorsa bunlar da görüşmede belirtilmelidir.</p>"],
      ["Kilo yönetimi ve takip", "<p>Kilo değişimi hedefleniyorsa enerji dengesi, protein ve lif alımı, hareket, uyku ve günlük yaşam birlikte değerlendirilir. Hızlı kilo kaybı yerine sürdürülebilir bir plan oluşturulur.</p>"]
    ],
    "related":"saglikli-tabak-nasil-hazirlanir",
    "source":"https://www.niddk.nih.gov/health-information/endocrine-diseases/hashimotos-disease"
  },
  {
    "slug":"lipodem-diyeti",
    "title":"Lipödem Diyeti ve Beslenme",
    "seo_title":"Lipödem Diyeti ve Beslenme | Online Diyetisyen",
    "meta_description":"Lipödemde beslenme; kilo yönetimi, yeterli protein-lif alımı, günlük öğün düzeni ve multidisipliner tedaviyi destekleyen sürdürülebilir alışkanlıklarla ele alınır.",
    "short":"Lipödem tanısı bulunan bireylerde tıbbi takip sürecine eşlik eden, sürdürülebilir beslenme ve kilo yönetimi desteği.",
    "intro":"Lipödem yalnızca beslenmeyle tedavi edilen bir durum değildir. Beslenme danışmanlığı; kilo yönetimi gerekiyorsa bunu desteklemek, yeterli ve dengeli öğünler oluşturmak ve günlük yaşamı kolaylaştırmak amacıyla multidisipliner sürecin bir parçası olarak ele alınır.",
    "sections":[
      ["Lipödemde beslenmenin rolü", "<p>Beslenme planının amacı lipödemi tek başına ortadan kaldırmak değildir. Genel sağlık, vücut ağırlığı yönetimi ve yeterli besin alımı desteklenir. Tedavi planı hekim ve gerekli diğer sağlık profesyonelleriyle birlikte yürütülmelidir.</p>"],
      ["Sürdürülebilir öğün düzeni", "<p>Sebze, meyve, tam tahıl, baklagil ve uygun protein kaynaklarının günlük yaşama yerleştirilmesi; yüksek oranda işlenmiş besinlerin sıklığının azaltılması kişisel koşullara göre ele alınabilir.</p>"],
      ["Ödem ve sıvı konusu", "<p>Sıvı ve sodyum düzeni kişisel sağlık durumuna göre değerlendirilir. Aşırı kısıtlayıcı detokslar veya hızlı sıvı kaybı vadeden yöntemler önerilmez.</p>"],
      ["Online takipte neler konuşulur?", "<p>Öğünlerin uygulanabilirliği, kilo yönetimi hedefi, hareket düzeyi, iş ve sosyal yaşam koşulları takip görüşmelerinde değerlendirilir ve plan gerektiğinde güncellenir.</p>"]
    ],
    "related":"tarti-yag-kas-ve-su-degisimi",
    "source":"https://www.ncbi.nlm.nih.gov/books/NBK573066/"
  },
  {
    "slug":"menopozda-beslenme",
    "title":"Menopozda Beslenme",
    "seo_title":"Menopozda Beslenme | Online Diyetisyen",
    "meta_description":"Menopozda beslenme; kilo yönetimi, protein, kalsiyum, D vitamini kaynakları, lif ve kalp sağlığını destekleyen öğünlerle kişiye göre planlanır.",
    "short":"Menopoz döneminde kilo yönetimi, kemik ve kalp sağlığı ile günlük yaşamı destekleyen kişisel beslenme danışmanlığı.",
    "intro":"Menopoz döneminde enerji gereksinimi, vücut kompozisyonu, kemik sağlığı ve kardiyometabolik riskler kişiden kişiye değişebilir. Beslenme planı yaş, hareket düzeyi, sağlık öyküsü ve günlük yaşamla birlikte ele alınır.",
    "sections":[
      ["Menopozda kilo yönetimi", "<p>Vücut ağırlığındaki değişimler yalnızca tek bir hormona bağlanmaz. Toplam enerji dengesi, kas kütlesi, hareket, uyku ve günlük alışkanlıklar birlikte değerlendirilir. Hedef hızlı kilo kaybı değil sürdürülebilir bir düzendir.</p>"],
      ["Protein, kalsiyum ve kemik sağlığı", "<p>Protein kaynaklarının gün içine dengeli dağılımı ile kalsiyum ve D vitamini gereksinimlerinin yeterliliği önemlidir. Takviye gereksinimi varsa hekim değerlendirmesiyle planlanır.</p>"],
      ["Lif ve kalp sağlığı", "<p>Sebze, meyve, tam tahıl, baklagil, yağlı tohumlar ve uygun yağ kaynaklarının dengeli kullanımı genel kardiyometabolik sağlığı destekleyen bir beslenme düzeninin parçasıdır.</p>"],
      ["Günlük hayata uyarlama", "<p>Sıcak basması, uyku düzeni, iştah değişiklikleri veya sosyal yaşam gibi kişisel durumlar konuşulur. Öğün planı bu günlük gerçekliğe göre şekillendirilir.</p>"]
    ],
    "related":"saglikli-tabak-nasil-hazirlanir",
    "source":"https://womenshealth.gov/menopause"
  },
  {
    "slug":"emzirme-doneminde-beslenme",
    "title":"Emzirme Döneminde Beslenme",
    "seo_title":"Emzirme Döneminde Beslenme | Online Diyetisyen",
    "meta_description":"Emzirme döneminde beslenme; annenin enerji, protein, sıvı ve mikrobesin gereksinimleri ile günlük yaşamına uygun pratik öğünler üzerinden kişisel olarak planlanır.",
    "short":"Emzirme döneminde annenin artan enerji ve besin gereksinimlerini günlük yaşama uygun biçimde ele alan beslenme danışmanlığı.",
    "intro":"Emzirme döneminde amaç katı yasaklar değil; annenin enerji, protein, sıvı ve mikrobesin gereksinimlerini karşılayan, pratik ve sürdürülebilir bir beslenme düzeni oluşturmaktır. Gereksinimler annenin sağlık durumu ve emzirme sürecine göre değişebilir.",
    "sections":[
      ["Emzirme döneminde enerji ve öğün düzeni", "<p>Günün koşullarına göre ana ve ara öğünler planlanabilir. Uykusuzluk, bebeğin bakım düzeni ve yemek hazırlamaya ayrılabilen zaman dikkate alınır. Her anneye aynı kalori veya aynı öğün sayısı önerilmez.</p>"],
      ["Protein, sıvı ve besin çeşitliliği", "<p>Yeterli protein, sebze-meyve, tahıl, süt veya uygun alternatifler ve yağ kaynakları dengeli biçimde ele alınır. Susama sinyallerine göre yeterli sıvı alımı desteklenir; aşırı sıvı tüketmenin süt miktarını otomatik artırdığı varsayılmaz.</p>"],
      ["Kilo verme hedefi varsa", "<p>Doğum sonrası kilo yönetimi hızlı ve kısıtlayıcı diyetlerle değil, annenin toparlanması ve emzirme süreci gözetilerek planlanır. Enerji kısıtlaması kişisel koşullara göre değerlendirilmelidir.</p>"],
      ["Takviyeler ve özel durumlar", "<p>Vitamin-mineral takviyeleri, vegan-vejetaryen beslenme, alerji veya kronik hastalık gibi özel durumlarda gereksinimler ayrıca değerlendirilir. Takviye kullanımı hekim önerileriyle uyumlu ele alınır.</p>"]
    ],
    "related":"saglikli-tabak-nasil-hazirlanir",
    "source":"https://www.cdc.gov/breastfeeding-special-circumstances/hcp/diet-micronutrients/maternal-diet.html"
  }
]

services=json.loads(services_path.read_text())
target_slugs={s['slug'] for s in new_services}
services=[s for s in services if s.get('slug') not in target_slugs]
services.extend(new_services)
services_path.write_text(json.dumps(services,ensure_ascii=False,indent=2)+'\n')

text=build_path.read_text()
url_map={
 'İnsülin Direncinde Beslenme':'/hizmetler/insulin-direncinde-beslenme/',
 'Haşimato Diyeti':'/hizmetler/hasimato-diyeti/',
 'Lipödem Diyeti':'/hizmetler/lipodem-diyeti/',
 'Menopozda Beslenme':'/hizmetler/menopozda-beslenme/',
 'Emzirme Döneminde Beslenme':'/hizmetler/emzirme-doneminde-beslenme/'
}
lines=[]
for line in text.splitlines():
    for title,url in url_map.items():
        if f"'title':'{title}'" in line:
            line=re.sub(r"'url':'[^']+'",f"'url':'{url}'",line)
    lines.append(line)
text='\n'.join(lines)+'\n'

old="out.append(f'<article class=\"service-card-v2\"><span class=\"service-icon-v2\" aria-hidden=\"true\">{e(s[\"icon\"])}</span><h3>{title}</h3><p>{e(s[\"short\"])}</p>'+('<ul>'+bullets+'</ul>' if bullets else '')+'</article>')"
new="out.append(f'<article class=\"service-card-v2\"><span class=\"service-icon-v2\" aria-hidden=\"true\">{e(s[\"icon\"])}</span><h3>{title}</h3><p>{e(s[\"short\"])}</p>'+('<ul>'+bullets+'</ul>' if bullets else '')+link(s['url'],'Detaylı İncele <span aria-hidden=\"true\">→</span>','service-detail-link')+'</article>')"
if old in text:
    text=text.replace(old,new,1)
elif 'service-detail-link' not in text:
    raise SystemExit('service card render target not found')

old_layout="layout('/hizmetler/'+s['slug']+'/',s['title']+' | Online Diyetisyen Tuğba',s['short']+' Tuğba Şeker Ağaç ile online ve Adana’da beslenme danışmanlığı.',body,extra=[schema])"
new_layout="layout('/hizmetler/'+s['slug']+'/',s.get('seo_title',s['title']+' | Online Diyetisyen Tuğba Şeker Ağaç'),s.get('meta_description',s['short']+' Tuğba Şeker Ağaç ile online ve Adana’da beslenme danışmanlığı.'),body,extra=[schema])"
if old_layout in text:
    text=text.replace(old_layout,new_layout,1)

text=text.replace('services-cards-v4','services-seo-v5')
build_path.write_text(text)

css=css_path.read_text()
marker='/* service-detail-links-2026-09-09 */'
if marker not in css:
    css += '''\n\n/* service-detail-links-2026-09-09 */\n.service-detail-link{display:inline-flex;align-items:center;justify-content:space-between;gap:16px;margin-top:20px;padding-top:14px;border-top:1px solid #dfe9df;color:#185b3a;font-size:13px;font-weight:700;letter-spacing:.01em}\n.service-detail-link:hover{color:#0f432b}\n.service-card-v2 .service-detail-link{margin-top:20px}\n'''
css_path.write_text(css)

site=json.loads(site_path.read_text())
site['updated']='2026-09-09'
updates=site.setdefault('page_updates',{})
for slug in target_slugs:
    updates[f'/hizmetler/{slug}/']='2026-09-09'
updates['/hizmetler/']='2026-09-09'
site_path.write_text(json.dumps(site,ensure_ascii=False,indent=2)+'\n')

print('Added 5 focused service pages, updated card URLs, SEO metadata and detail links.')
