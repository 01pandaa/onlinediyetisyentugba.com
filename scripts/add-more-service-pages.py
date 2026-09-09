#!/usr/bin/env python3
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
services_path=ROOT/'content/services.json'
build_path=ROOT/'scripts/build.py'
site_path=ROOT/'content/site.json'

new_services=[
  {
    "slug":"pcos-beslenmesi",
    "title":"Polikistik Over Sendromu (PCOS) Beslenmesi",
    "seo_title":"PCOS Beslenmesi | Online Diyetisyen Tuğba Şeker Ağaç",
    "meta_description":"PCOS'ta beslenme; öğün düzeni, kilo yönetimi, insülin direnci, lif ve protein dengesi ile kişisel sağlık öyküsüne göre planlanır.",
    "short":"PCOS tanısı bulunan bireylerde günlük beslenme düzeni, kilo yönetimi ve insülin direncini dikkate alan kişisel danışmanlık.",
    "intro":"PCOS'ta tek bir yasak listesi veya herkese uyan standart bir diyet yoktur. Beslenme yaklaşımı; kilo yönetimi gereksinimi, insülin direnci, adet düzeni, günlük yaşam, kullanılan ilaçlar ve hekim takibi birlikte değerlendirilerek planlanır.",
    "sections":[
      ["PCOS'ta beslenme yaklaşımı", "<p>Öğün içeriği ve zamanlaması kişisel yaşam düzenine göre ele alınır. Sebze, tam tahıl, baklagil ve diğer lif kaynakları ile uygun protein kaynaklarının dengelenmesi üzerinde çalışılır. Tek bir besinin veya takviyenin PCOS'u tedavi ettiği iddia edilmez.</p>"],
      ["İnsülin direnci ve kilo yönetimi", "<p>İnsülin direnci veya kilo yönetimi gereksinimi varsa hızlı ve aşırı kısıtlayıcı diyetler yerine sürdürülebilir bir enerji dengesi hedeflenir. Hareket, uyku ve günlük stres de sürecin uygulanabilirliğini etkileyebilir.</p>"],
      ["Takipte neler değerlendirilir?", "<ul><li>Öğünlerin uygulanabilirliği ve açlık-tokluk durumu.</li><li>Besin çeşitliliği ve porsiyonlar.</li><li>Hekim tarafından izlenen laboratuvar sonuçları ve tedavi planı.</li><li>Günlük yaşam ve sosyal ortama uyum.</li></ul>"],
      ["Online diyetisyen desteği", "<p>Online görüşmelerde plan günlük rutininize göre hazırlanır; takipte uygulanamayan noktalar yeniden düzenlenir. İlaç tedavisi veya hormonal tedaviye diyetisyen tarafından müdahale edilmez.</p>"]
    ],
    "related":"insulin-direncinde-beslenme",
    "source":"https://womenshealth.gov/a-z-topics/polycystic-ovary-syndrome"
  },
  {
    "slug":"diyabet-beslenmesi",
    "title":"Diyabet Beslenmesi",
    "seo_title":"Diyabet Beslenmesi | Online Diyetisyen",
    "meta_description":"Diyabette beslenme; karbonhidrat kaynakları, öğün düzeni, lif-protein dengesi ve kullanılan tedaviyle uyumlu kişisel planlama üzerinden ele alınır.",
    "short":"Diyabette kan şekeri yönetimini destekleyen, tedavi planı ve günlük yaşama göre kişiselleştirilen beslenme danışmanlığı.",
    "intro":"Diyabet beslenmesinde amaç yasaklarla ilerlemek değil; karbonhidrat kaynaklarını, porsiyonları, öğün zamanlamasını ve günlük yaşamı kullanılan tedaviyle birlikte değerlendirmektir. Plan diyabet tipi, ilaç veya insülin kullanımı ve bireysel gereksinimlere göre değişir.",
    "sections":[
      ["Karbonhidratları nasıl ele alıyoruz?", "<p>Karbonhidrat içeren besinlerin türü, miktarı ve öğünlere dağılımı kişiye göre değerlendirilir. Tam tahıl, sebze, meyve ve baklagil gibi lif kaynaklarının uygun porsiyonlarda kullanımı desteklenebilir.</p>"],
      ["İlaç ve insülin kullananlarda dikkat", "<p>İnsülin veya hipoglisemi riski taşıyan ilaçlar kullanılıyorsa öğün değişiklikleri sağlık ekibiyle uyumlu yürütülmelidir. İlaç veya insülin dozu diyetisyen tarafından değiştirilmez.</p>"],
      ["Günlük yaşam ve takip", "<p>İş saatleri, dışarıda yemek, fiziksel aktivite ve uyku düzeni planın uygulanabilirliğini etkiler. Takip görüşmelerinde öğünlerin nasıl gittiği ve hangi noktalarda düzenleme gerektiği konuşulur.</p>"],
      ["Online görüşmede neler konuşulur?", "<ul><li>Öğün saatleri ve porsiyonlar.</li><li>Karbonhidrat kaynakları ve lif alımı.</li><li>Hipoglisemi öyküsü ve günlük rutin.</li><li>Hekim tarafından izlenen güncel sağlık bilgileri.</li></ul>"]
    ],
    "related":"insulin-direncinde-beslenme",
    "source":"https://www.niddk.nih.gov/health-information/diabetes/overview/diet-eating-physical-activity"
  },
  {
    "slug":"eliminasyon-diyeti",
    "title":"Eliminasyon Diyeti",
    "seo_title":"Eliminasyon Diyeti | Online Diyetisyen",
    "meta_description":"Eliminasyon diyeti; gerekli durumlarda belirli besinlerin kontrollü olarak çıkarılması, belirtilerin izlenmesi ve uygun şekilde yeniden değerlendirilmesiyle planlanır.",
    "short":"Gerekli görülen durumlarda besin toleransını değerlendirmek için kontrollü ve süreli biçimde planlanan eliminasyon süreci.",
    "intro":"Eliminasyon diyeti rastgele çok sayıda besini uzun süre çıkarmak anlamına gelmez. Hangi besinlerin ne kadar süreyle çıkarılacağı, belirtilerin nasıl izleneceği ve yeniden deneme aşaması kişisel sağlık öyküsüne göre planlanır.",
    "sections":[
      ["Eliminasyon ne zaman düşünülür?", "<p>Belirli sindirim yakınmaları, hekim tarafından değerlendirilen intolerans şüphesi veya başka tıbbi gerekçelerde kontrollü eliminasyon gündeme gelebilir. Şiddetli, yeni başlayan veya açıklanamayan belirtilerde öncelikle hekim değerlendirmesi gerekir.</p>"],
      ["Süre ve yeniden deneme neden önemlidir?", "<p>Gereksiz ve uzun süreli kısıtlamalar besin çeşitliliğini azaltabilir. Bu nedenle eliminasyon mümkün olduğunca hedefli, süreli ve yeniden değerlendirme adımı içeren bir süreç olmalıdır.</p>"],
      ["Besin günlüğü ve belirti takibi", "<p>Öğünler, belirtilerin zamanı ve şiddeti not edilebilir. Tek bir gün veya tek bir besin üzerinden kesin sonuç çıkarılmaz; örüntüler zaman içinde değerlendirilir.</p>"],
      ["Online takip", "<p>Online görüşmelerde alışveriş, dışarıda yemek, tarif alternatifleri ve yeniden deneme aşaması günlük yaşama göre planlanır. Gerektiğinde hekim veya ilgili sağlık profesyoneline yönlendirme yapılır.</p>"]
    ],
    "related":"saglikli-tabak-nasil-hazirlanir",
    "source":"https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome/eating-diet-nutrition"
  },
  {
    "slug":"glutensiz-beslenme",
    "title":"Glutensiz Beslenme",
    "seo_title":"Glutensiz Beslenme | Online Diyetisyen",
    "meta_description":"Glutensiz beslenme; çölyak hastalığı veya tıbbi gereklilik bulunan durumlarda güvenli ürün seçimi, etiket okuma ve dengeli öğün planlamasıyla ele alınır.",
    "short":"Çölyak tanısı veya tıbbi gereklilik bulunan durumlarda güvenli ve dengeli glutensiz beslenme düzeni oluşturma desteği.",
    "intro":"Glutensiz beslenme özellikle çölyak hastalığında tedavinin temel parçasıdır. Ancak tıbbi gerekçe olmadan gluten içeren tüm besinleri çıkarmak herkes için gerekli değildir. Plan; güvenli ürün seçimi, çapraz bulaş riski, etiket okuma ve besin çeşitliliği dikkate alınarak hazırlanır.",
    "sections":[
      ["Hangi besinler doğal olarak glutensizdir?", "<p>Pirinç, patates, mısır, karabuğday, baklagiller, sebze, meyve, et, yumurta ve süt ürünlerinin pek çoğu doğal olarak gluten içermez. Paketli ürünlerde ise içerik ve üretim koşulları ayrıca kontrol edilmelidir.</p>"],
      ["Etiket okuma ve çapraz bulaş", "<p>Çölyak hastalığında yalnızca içerik değil, üretim ve hazırlama sırasında çapraz bulaş olasılığı da önemlidir. Evde, restoranda ve alışverişte güvenli uygulamalar kişiye göre konuşulur.</p>"],
      ["Besin çeşitliliğini korumak", "<p>Glutensiz ürün seçerken lif, protein, demir ve diğer mikrobesinlerin yeterliliği gözden geçirilir. Sadece paketli glutensiz ürünlere dayalı tekdüze bir düzen önerilmez.</p>"],
      ["Online danışmanlıkta destek", "<p>Market ürünleri, mutfak düzeni, dışarıda yemek ve pratik öğün alternatifleri günlük yaşama göre ele alınır. Çölyak tanısı ve tıbbi takip hekim tarafından yürütülür.</p>"]
    ],
    "related":"saglikli-tabak-nasil-hazirlanir",
    "source":"https://www.niddk.nih.gov/health-information/digestive-diseases/celiac-disease/eating-diet-nutrition"
  },
  {
    "slug":"cocuk-ergen-beslenmesi",
    "title":"Çocuk ve Ergen Beslenmesi",
    "seo_title":"Çocuk ve Ergen Beslenmesi | Diyetisyen Tuğba Şeker Ağaç",
    "meta_description":"Çocuk ve ergen beslenmesi; büyüme-gelişme, okul düzeni, aile alışkanlıkları ve yaşa uygun besin çeşitliliği üzerinden kişisel olarak değerlendirilir.",
    "short":"Büyüme ve gelişme döneminde yaşa, okul düzenine ve aile yaşamına uygun beslenme alışkanlıklarını destekleyen danışmanlık.",
    "intro":"Çocuk ve ergenlerde beslenme yalnızca kilo üzerinden değerlendirilmez. Büyüme-gelişme, yaş, aktivite, okul düzeni, aile sofraları, sağlık öyküsü ve yeme davranışı birlikte ele alınır. Amaç çocuğun gereksinimlerini karşılayan, aile içinde uygulanabilir bir düzen oluşturmaktır.",
    "sections":[
      ["Büyüme ve gelişme önceliklidir", "<p>Çocuk ve ergenlerde enerji ve besin gereksinimleri yaşa, büyüme hızına ve aktivite düzeyine göre değişir. Yetişkinlere yönelik hızlı kilo verme diyetleri doğrudan çocuklara uygulanmaz.</p>"],
      ["Okul ve günlük yaşam", "<p>Kahvaltı, okul öğünü, kantin seçenekleri, spor saatleri ve evdeki yemek düzeni birlikte değerlendirilir. Pratik ve ulaşılabilir alternatifler aileyle birlikte planlanır.</p>"],
      ["Aile yaklaşımı ve yeme davranışı", "<p>Besinleri ödül-ceza aracı yapmak veya çocuğu sürekli kilosu üzerinden eleştirmek yerine, düzenli öğün ortamı ve çeşitli besinlerle karşılaşma desteklenir. Gerektiğinde ilgili sağlık profesyonelleriyle birlikte çalışılır.</p>"],
      ["Ne zaman hekim değerlendirmesi gerekir?", "<p>Belirgin büyüme geriliği, hızlı ve açıklanamayan kilo değişimi, yutma güçlüğü, sürekli kusma, ciddi besin reddi veya başka sağlık belirtilerinde çocuk hekimi değerlendirmesi önceliklidir.</p>"]
    ],
    "related":"saglikli-tabak-nasil-hazirlanir",
    "source":"https://www.cdc.gov/healthy-weight-growth/healthy-eating/index.html"
  }
]

services=json.loads(services_path.read_text())
target_slugs={s['slug'] for s in new_services}
services=[s for s in services if s.get('slug') not in target_slugs]
services.extend(new_services)
services_path.write_text(json.dumps(services,ensure_ascii=False,indent=2)+'\n')

text=build_path.read_text()
replacements={
  "'title':'Polikistik Over (PCOS)'":"'title':'Polikistik Over (PCOS)'",
  "'title':'Polikistik Over (PCOS)','short'":"'title':'Polikistik Over (PCOS)','short'"
}
url_targets={
  "'title':'Polikistik Over (PCOS)'":"/hizmetler/pcos-beslenmesi/",
  "'title':'Diyabet Beslenmesi'":"/hizmetler/diyabet-beslenmesi/",
  "'title':'Eliminasyon Diyeti'":"/hizmetler/eliminasyon-diyeti/",
  "'title':'Glutensiz Beslenme'":"/hizmetler/glutensiz-beslenme/",
  "'title':'Çocuk ve Ergen Beslenmesi'":"/hizmetler/cocuk-ergen-beslenmesi/"
}
for marker,new_url in url_targets.items():
    pattern=r"(\{[^\n]*"+re.escape(marker)+r"[^\n]*'url':)'[^']*'"
    text,n=re.subn(pattern,lambda m:m.group(1)+repr(new_url),text,count=1)
    if n!=1:
        raise SystemExit(f'Card link target not found: {marker}')
build_path.write_text(text)

site=json.loads(site_path.read_text())
site['updated']='2026-09-09'
updates=site.setdefault('page_updates',{})
updates['/hizmetler/']='2026-09-09'
for s in new_services:
    updates['/hizmetler/'+s['slug']+'/']='2026-09-09'
site_path.write_text(json.dumps(site,ensure_ascii=False,indent=2)+'\n')

print('Added 5 focused service pages and updated service-card links.')
