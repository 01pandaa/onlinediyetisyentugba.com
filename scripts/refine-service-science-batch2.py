#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
services_path = ROOT / 'content' / 'services.json'
build_path = ROOT / 'scripts' / 'build.py'
site_path = ROOT / 'content' / 'site.json'

services = json.loads(services_path.read_text())

updates = {
    'kilo-verme': {
        'title': 'Kilo Verme ve Kilo Yönetimi',
        'seo_title': 'Kilo Verme ve Kilo Yönetimi | Online Diyetisyen',
        'meta_description': 'Kilo verme sürecinde enerji dengesi, kas kütlesinin korunması, protein-lif dengesi, uyku, hareket ve sürdürülebilir alışkanlıklar birlikte değerlendirilir.',
        'short': 'Kilo kaybını yalnızca tartıya değil, beslenme kalitesi, kas kütlesi, günlük yaşam ve sürdürülebilir alışkanlıklara göre ele alan kişisel planlama.',
        'intro': 'Kilo verme süreci yalnızca daha az yemek veya tartıda hızlı düşüş görmek değildir. Bilimsel yaklaşım; kişiye uygun bir enerji dengesi oluşturmayı, beslenme kalitesini artırmayı, yağ kaybı sırasında kas kütlesini mümkün olduğunca korumayı ve verilen kilonun sürdürülebilirliğini birlikte ele alır.',
        'sections': [
            ['Kilo kaybının temel mekanizması: enerji dengesi', '<p>Vücut ağırlığının azalması için uzun vadede alınan enerji ile harcanan enerji arasında kişiye uygun bir fark oluşması gerekir. Ancak bu, herkesin kalori sayması gerektiği anlamına gelmez. Porsiyon düzeni, öğün yapısı, içecekler, atıştırmalar, besin yoğunluğu ve günlük hareket birlikte ele alınarak daha uygulanabilir bir enerji dengesi kurulabilir.</p><p>Çok hızlı ve aşırı kısıtlayıcı diyetler kısa vadede tartıda belirgin düşüş yaratabilse de açlık, yorgunluk, kas kaybı ve diyeti sürdürememe riskini artırabilir. Bu nedenle hedef, mümkün olan en hızlı kayıp değil; sürdürülebilir bir değişimdir.</p>'],
            ['Tartıdaki her değişim yağ kaybı değildir', '<p>Vücut ağırlığı; yağ dokusu, kas dokusu, glikojen, sindirim sistemi içeriği ve vücut suyundan etkilenir. Özellikle tuz tüketimi, karbonhidrat miktarı, adet döngüsü, egzersiz ve bağırsak düzeni birkaç gün içinde tartıda değişiklik oluşturabilir.</p><p>Bu nedenle tek bir tartı sonucu yerine haftalar içindeki eğilim, bel çevresi gibi ölçümler, kıyafetlerin duruşu, enerji düzeyi ve beslenme planının sürdürülebilirliği birlikte değerlendirilir.</p>'],
            ['Protein, lif ve tokluk ilişkisi', '<p>Yeterli protein ve lif içeren öğünler tokluk yönetimini kolaylaştırabilir. Yumurta, yoğurt/kefir, balık, et, tavuk, baklagiller ve uygun bitkisel protein kaynakları; sebze, meyve, tam tahıl ve kurubaklagillerle birlikte planlandığında öğünlerin besin kalitesi artar.</p><p>Protein miktarı kişiye göre belirlenir. Daha fazla protein her zaman daha fazla yağ kaybı anlamına gelmez; toplam beslenme düzeni, böbrek sağlığı, aktivite düzeyi ve kişisel gereksinimler dikkate alınmalıdır.</p>'],
            ['Kas kütlesini korumak neden önemlidir?', '<p>Kilo verirken amaç yalnızca vücut ağırlığını azaltmak değil, mümkün olduğunca yağ dokusundan kayıp sağlarken yağsız vücut kütlesini korumaktır. Yeterli protein, günlük hareket ve kişinin sağlık durumuna uygun direnç egzersizleri bu açıdan önem taşır.</p><p>Kas kütlesinin korunması fiziksel işlev, güç, günlük enerji harcaması ve uzun dönem kilo yönetimi açısından değerlidir. Egzersiz planı kişinin sağlık durumuna göre hekim veya egzersiz profesyoneliyle birlikte düzenlenebilir.</p>'],
            ['Uyku, stres ve günlük hareket de planın parçasıdır', '<p>Uyku süresi ve kalitesi, stres düzeyi, masa başında geçirilen süre ve günlük adım/hareket miktarı yeme davranışını ve enerji dengesini etkileyebilir. Bu nedenle yalnızca “ne yediğiniz” değil, günün nasıl geçtiği de görüşmelerde değerlendirilir.</p><p>Vardiya, yoğun iş temposu, seyahat, sosyal yemekler veya hafta sonu düzeni için gerçekçi alternatifler oluşturulur.</p>'],
            ['Takipte başarıyı nasıl değerlendiriyoruz?', '<p>Belirli bir sürede belirli kilogram verme garantisi verilmez. Kilo değişiminin yanı sıra öğün düzeninin oturması, açlık-tokluk kontrolü, sebze ve protein tüketimi, hareket alışkanlığı, uyku, sindirim yakınmaları ve planın günlük hayatta uygulanabilirliği de izlenir.</p>']
        ]
    },
    'kilo-alma': {
        'title': 'Sağlıklı Kilo Alma',
        'seo_title': 'Sağlıklı Kilo Alma | Online Diyetisyen',
        'meta_description': 'Sağlıklı kilo alma sürecinde enerji yoğunluğu, protein, öğün sıklığı, kas kütlesi, sindirim toleransı ve olası besin yetersizlikleri kişiye göre değerlendirilir.',
        'short': 'Kilo alma hedefinde yalnızca daha fazla yemek değil; enerji, protein, kas kütlesi, sindirim toleransı ve besin kalitesini birlikte ele alan kişisel yaklaşım.',
        'intro': 'Sağlıklı kilo alma sürecinde amaç yalnızca tartıdaki sayıyı yükseltmek değildir. Enerji ve protein gereksinimini karşılayan, sindirim sistemini zorlamayan, besin öğesi yeterliliğini koruyan ve mümkün olduğunda kas kütlesini destekleyen bir plan oluşturulur. Açıklanamayan veya istemsiz kilo kaybında önce tıbbi nedenlerin araştırılması gerekir.',
        'sections': [
            ['Önce düşük kilonun veya kilo kaybının nedeni değerlendirilir', '<p>Uzun yıllardır düşük vücut ağırlığında olmak ile son aylarda istemsiz kilo kaybetmek aynı durum değildir. İştahsızlık, tiroid hastalıkları, sindirim sistemi sorunları, enfeksiyonlar, depresyon, kullanılan ilaçlar veya başka tıbbi durumlar kilo kaybına eşlik edebilir.</p><p>Özellikle hızlı ve açıklanamayan kilo kaybı, belirgin iştahsızlık, sürekli ishal, kusma, yutma güçlüğü veya ciddi halsizlik varsa yalnızca beslenme planıyla ilerlemek yerine hekim değerlendirmesi gerekir.</p>'],
            ['Enerji yoğunluğunu artırmak ne demektir?', '<p>Kilo almak için porsiyonları kontrolsüz biçimde büyütmek yerine, öğünlerin enerji ve besin yoğunluğu artırılabilir. Zeytinyağı, tahin, avokado, kuruyemişler, yoğurt, peynir, yumurta, baklagiller ve uygun tahıl kaynakları kişisel toleransa göre kullanılabilir.</p><p>Çabuk doyan kişilerde üç çok büyük öğün yerine daha küçük ana öğünler ve planlı ara öğünler daha kolay uygulanabilir. Sıvı öğünler veya smoothie benzeri seçenekler gerektiğinde destekleyici olabilir; ancak tüm beslenmenin sıvı ürünlere dayanması hedeflenmez.</p>'],
            ['Protein ve kas kütlesi', '<p>Kilo artışının mümkün olduğunca işlevsel doku kazanımını desteklemesi için yeterli protein önemlidir. Protein gereksinimi yaşa, vücut ağırlığına, aktiviteye ve sağlık durumuna göre değişir.</p><p>Sağlık durumu uygunsa direnç egzersizi ile yeterli enerji-protein alımının birlikte planlanması kas kütlesinin artışını destekleyebilir. Yalnızca yüksek kalorili işlenmiş ürünlerle kilo almak beslenme kalitesini artırmaz.</p>'],
            ['Mikrobesin yeterliliği gözden kaçmamalıdır', '<p>Düşük enerji alımı demir, B12, folat, D vitamini, kalsiyum, çinko ve diğer besin öğelerinin yetersizliğiyle birlikte görülebilir. Kişinin beslenme öyküsü ve varsa laboratuvar sonuçları değerlendirilerek eksiklik şüphesi varsa uygun sağlık profesyoneline yönlendirme yapılır.</p><p>Takviyeler yalnızca kilo almak amacıyla rastgele başlanmaz.</p>'],
            ['Sindirim toleransı ve iştah yönetimi', '<p>Şişkinlik, erken doyma, reflü, kabızlık veya ishal gibi yakınmalar büyük porsiyonları zorlaştırabilir. Öğün hacmi, yağ miktarı, lif düzeyi ve öğün zamanlaması kişisel toleransa göre düzenlenir.</p><p>Belirtiler yeni başladıysa veya giderek artıyorsa altta yatan nedeni değerlendirmek için tıbbi inceleme gerekebilir.</p>'],
            ['Takipte yalnızca kilo değil vücut işlevi de izlenir', '<p>İzlemde kilo değişiminin yanı sıra iştah, öğünleri tamamlayabilme, güç ve enerji hissi, sindirim toleransı, fiziksel aktivite ve planın sürdürülebilirliği değerlendirilir. Çok hızlı kilo artışı hedeflenmez; artışın hızı kişisel duruma göre planlanır.</p>']
        ]
    },
    'sporcu-beslenmesi': {
        'title': 'Sporcu Beslenmesi ve Aktif Yaşam',
        'seo_title': 'Sporcu Beslenmesi | Online Diyetisyen',
        'meta_description': 'Sporcu beslenmesinde enerji kullanılabilirliği, karbonhidrat ve protein dağılımı, antrenman çevresi öğünleri, hidrasyon ve takviye güvenliği kişiye göre planlanır.',
        'short': 'Antrenman yükü, enerji kullanılabilirliği, karbonhidrat-protein dengesi, toparlanma ve sıvı gereksinimlerini kişiselleştiren sporcu beslenmesi desteği.',
        'intro': 'Sporcu beslenmesi yalnızca protein miktarını artırmak değildir. Antrenman türü, süresi ve yoğunluğuna göre enerji kullanılabilirliği, karbonhidrat depoları, protein dağılımı, sıvı-elektrolit dengesi ve toparlanma birlikte değerlendirilir. Rekreatif spor yapan biriyle yarışmacı bir sporcunun gereksinimleri aynı değildir.',
        'sections': [
            ['Enerji kullanılabilirliği neden temel konudur?', '<p>Uzun süre antrenman yüküne göre yetersiz enerji almak performans düşüşü, toparlanma sorunları, hormonal değişiklikler, kemik sağlığında bozulma ve sık sakatlanma gibi sorunlarla ilişkilidir. Sporcularda yalnızca kilo veya yağ oranına odaklanmak bu nedenle yeterli değildir.</p><p>Antrenman hacmi arttığında öğünlerin ve ara öğünlerin de buna uyarlanması gerekir. Özellikle hızlı kilo verme hedefleri veya uzun süreli açlık dönemleri sporcularda dikkatle değerlendirilmelidir.</p>'],
            ['Karbonhidrat: antrenmanın yakıtı', '<p>Karbonhidrat gereksinimi yapılan sporun türüne ve antrenman süresine göre değişir. Dayanıklılık veya yüksek yoğunluklu antrenmanlarda kas glikojeni önemli bir enerji kaynağıdır. Bu nedenle karbonhidratı tamamen kesmek yerine miktarını ve zamanlamasını antrenman yüküne göre ayarlamak daha doğru bir yaklaşımdır.</p><p>Antrenman öncesi ve sonrası öğünler gastrointestinal tolerans, hedef ve antrenman saatine göre kişiselleştirilir.</p>'],
            ['Protein: toplam miktar kadar gün içine dağılım da önemlidir', '<p>Protein kas onarımı ve adaptasyonu için gereklidir. Ancak tek bir öğünde çok yüksek protein almak yerine günlük gereksinimin ana öğünlere ve gerektiğinde ara öğünlere dağıtılması daha işlevsel olabilir.</p><p>Protein kaynağı olarak süt ürünleri, yumurta, et, balık, tavuk, baklagiller, soya ürünleri ve diğer uygun bitkisel seçenekler kullanılabilir. Gereksinim besinlerle karşılanabiliyorsa protein tozu zorunlu değildir.</p>'],
            ['Hidrasyon kişiye göre değişir', '<p>Sıvı gereksinimi hava sıcaklığı, nem, antrenman süresi, terleme hızı, kıyafet ve kişisel fizyolojiye göre değişebilir. Bu nedenle herkese aynı litre hedefini vermek yerine antrenman öncesi-sonrası vücut ağırlığı değişimi, idrar rengi ve terleme özellikleri birlikte değerlendirilebilir.</p><p>Uzun ve yoğun egzersizlerde yalnızca su değil sodyum ve karbonhidrat gereksinimi de gündeme gelebilir. Aşırı su tüketimi de risk oluşturabileceğinden “ne kadar çok o kadar iyi” yaklaşımı kullanılmaz.</p>'],
            ['Takviyelerde önce güvenlik', '<p>Sporcu takviyelerinin yararı ürün ve kullanım amacına göre değişir. Bazı ürünlerde kanıt sınırlıdır; ayrıca içerik hatası veya yasaklı madde kontaminasyonu riski bulunabilir. Yarışmacı sporcularda üçüncü taraf testinden geçmiş ürünler ve ilgili antidoping kuralları önemlidir.</p><p>Takviye planlaması beslenmedeki eksikler, antrenman hedefi, kullanılan ilaçlar ve sağlık durumu değerlendirilmeden yapılmaz.</p>'],
            ['Takipte neleri izliyoruz?', '<ul><li>Antrenman öncesi ve sonrası enerji düzeyi.</li><li>Toparlanma ve kas ağrısı.</li><li>Uyku, iştah ve gastrointestinal tolerans.</li><li>Antrenman günleri ile dinlenme günlerinde öğün düzeni.</li><li>Gerektiğinde vücut ağırlığı ve vücut kompozisyonundaki eğilim.</li></ul><p>Performans artışı için kesin sonuç garantisi verilmez; beslenme planı antrenman programıyla birlikte düzenli olarak güncellenir.</p>']
        ]
    },
    'gebelik-emzirme-beslenmesi': {
        'title': 'Gebelikte Beslenme',
        'seo_title': 'Gebelikte Beslenme | Online Diyetisyen',
        'meta_description': 'Gebelikte beslenme; gebelik haftası, başlangıç vücut ağırlığı, kilo artışı, folat-demir-iyot-B12-D vitamini gereksinimleri, bulantı ve kan şekeri yönetimi dikkate alınarak planlanır.',
        'short': 'Gebelik haftası, başlangıç vücut ağırlığı, besin öğesi gereksinimleri, bulantı ve kan şekeri gibi değişkenleri hekim takibiyle birlikte ele alan kişisel planlama.',
        'intro': 'Gebelikte beslenmenin amacı “iki kişilik yemek” değil; anne adayının ve bebeğin gereksinimlerini karşılayan, uygun gebelik kilo artışını destekleyen ve besin güvenliğini gözeten dengeli bir düzen oluşturmaktır. Gebelik haftası, gebelik öncesi vücut ağırlığı, laboratuvar sonuçları, bulantı-kusma, kan şekeri ve hekim önerileri birlikte değerlendirilir.',
        'sections': [
            ['Gebelikte enerji ihtiyacı nasıl değişir?', '<p>Gebelikte enerji gereksinimi trimester ilerledikçe artabilir ancak bu artış herkeste aynı değildir. “İki kişilik yemek” yaklaşımı gereksiz kilo artışına yol açabilir. Başlangıç vücut ağırlığı, gebelik haftası, günlük hareket ve çoğul gebelik gibi faktörler dikkate alınır.</p><p>Gebelikte kilo artışı tek başına estetik bir konu değildir; hem yetersiz hem aşırı kilo artışı anne ve bebek açısından risklerle ilişkilidir. Hedef aralık kadın doğum ekibinin takibiyle, gebelik öncesi vücut ağırlığı/BKİ ve klinik duruma göre değerlendirilir.</p>'],
            ['Folat, demir, iyot, B12 ve D vitamini neden önemlidir?', '<p>Gebelikte bazı mikrobesin gereksinimleri artar. Folat nöral tüp gelişimi için, demir artan kan hacmi ve fetal gelişim için, iyot tiroid hormonları ve nörogelişim için önemlidir. B12 ve D vitamini de kişisel beslenme biçimi ve laboratuvar durumuna göre değerlendirilmelidir.</p><p>Takviye dozu internetten veya başka bir gebeden kopyalanmamalıdır. Prenatal vitamin ve mineral desteği kadın doğum hekiminin önerisi, kullanılan diğer takviyeler ve laboratuvar sonuçlarıyla birlikte planlanmalıdır.</p>'],
            ['Protein, lif ve yağ kalitesi', '<p>Yumurta, iyi pişmiş et/tavuk, uygun balık seçenekleri, süt ürünleri, baklagiller ve güvenli bitkisel protein kaynakları protein gereksinimine katkı sağlar. Tam tahıllar, sebzeler, meyveler ve kurubaklagiller lif alımını destekleyebilir.</p><p>Zeytinyağı, ceviz, avokado ve uygun balık türleri gibi doymamış yağ kaynakları dengeli biçimde kullanılabilir. Balık tüketiminde cıva riski düşük türlerin seçimi ve güncel ulusal/klinik öneriler önemlidir.</p>'],
            ['Bulantı, reflü ve kabızlıkta beslenme düzeni', '<p>Özellikle ilk trimesterde bulantı ve koku hassasiyeti, ilerleyen haftalarda reflü veya kabızlık görülebilir. Küçük ve sık öğünler, mideyi uzun süre boş bırakmamak, yağlı-ağır öğünleri azaltmak, yeterli sıvı ve lif almak kişiye göre yardımcı olabilir.</p><p>Şiddetli kusma, sıvı alamama, hızlı kilo kaybı veya belirgin halsizlik durumunda hiperemezis gibi tıbbi durumların değerlendirilmesi için hekime başvurulmalıdır.</p>'],
            ['Gestasyonel diyabet veya yüksek kan şekeri varsa', '<p>Gestasyonel diyabet tanısı konduğunda amaç karbonhidratı tamamen kesmek değildir. Karbonhidratın türü, porsiyonu ve gün içine dağılımı; kan şekeri ölçümleri, gebelik haftası ve tedavi planına göre düzenlenir.</p><p>İlaç veya insülin gereksinimine yalnızca hekim karar verir. Diyetisyen beslenme planını sağlık ekibinin tedavisiyle uyumlu hâle getirir.</p>'],
            ['Besin güvenliği gebelikte ayrıca önemlidir', '<p>Çiğ veya az pişmiş et-yumurta, pastörize edilmemiş süt ürünleri ve uygun saklanmamış gıdalar gıda kaynaklı enfeksiyon riskini artırabilir. Sebze ve meyvelerin iyi yıkanması, soğuk zincirin korunması ve mutfakta çapraz bulaşmanın önlenmesi önemlidir.</p><p>Bitki çayları, “detoks” ürünleri ve yüksek doz bitkisel takviyeler gebelikte otomatik olarak güvenli kabul edilmemelidir.</p>']
        ]
    }
}

for item in services:
    if item.get('slug') in updates:
        item.update(updates[item['slug']])

vegan_slug = 'vejetaryen-vegan-beslenme'
if not any(item.get('slug') == vegan_slug for item in services):
    services.append({
        'slug': vegan_slug,
        'title': 'Vejetaryen ve Vegan Beslenme',
        'seo_title': 'Vejetaryen ve Vegan Beslenme | Online Diyetisyen',
        'meta_description': 'Vejetaryen ve vegan beslenmede protein kalitesi, B12, demir, iyot, çinko, kalsiyum, D vitamini ve omega-3 yeterliliğini gözeten kişisel planlama.',
        'short': 'Bitkisel ağırlıklı beslenmede protein ve kritik mikrobesinleri yeterli düzeyde karşılamaya odaklanan bilimsel ve kişiselleştirilmiş planlama.',
        'intro': 'Vejetaryen ve vegan beslenme doğru planlandığında yüksek besin kalitesine sahip olabilir; ancak yalnızca hayvansal ürünleri çıkarmak dengeli bir beslenme planı oluşturmaz. Protein çeşitliliği, B12, demir, iyot, çinko, kalsiyum, D vitamini ve omega-3 gibi besin öğeleri özellikle değerlendirilir.',
        'sections': [
            ['Bitkisel beslenmenin kalitesi nasıl değerlendirilir?', '<p>Bitkisel beslenme; sebze, meyve, tam tahıl, baklagil, kuruyemiş ve tohumlardan zengin olduğunda lif ve birçok fitokimyasal açısından güçlü olabilir. Ancak vegan etiketli ultra işlenmiş ürünlerin fazla tüketilmesi beslenme kalitesini otomatik olarak yükseltmez.</p><p>Planın temelini mümkün olduğunca az işlenmiş bitkisel besinler oluşturur; hazır vegan ürünler ise içerik, protein, tuz ve doymuş yağ miktarına göre değerlendirilir.</p>'],
            ['Protein yeterliliği ve aminoasit çeşitliliği', '<p>Mercimek, nohut, kuru fasulye, soya ve soya ürünleri, bezelye, tahıllar, kuruyemişler ve tohumlar bitkisel protein kaynaklarıdır. Gün içinde farklı kaynakların tüketilmesi aminoasit çeşitliliğini destekler.</p><p>Her öğünde kusursuz “protein eşleştirmesi” yapmak gerekmez; önemli olan günün toplamında yeterli enerji ve protein alınmasıdır. Sporcularda, ileri yaşta veya gebelik gibi özel dönemlerde gereksinim ayrıca değerlendirilir.</p>'],
            ['B12 vitamini vegan beslenmede kritik bir konudur', '<p>Güvenilir B12 kaynakları vegan beslenmede sınırlıdır. Bu nedenle vegan bireylerde B12 ile zenginleştirilmiş ürünler ve/veya uygun B12 takviyesi genellikle planın temel parçasıdır. Takviye dozu kişinin kullandığı ürüne, laboratuvar sonuçlarına ve sağlık durumuna göre belirlenmelidir.</p><p>B12 eksikliği yalnızca kansızlık değil nörolojik sorunlarla da ilişkili olabileceği için uzun süre kontrolsüz bırakılmamalıdır.</p>'],
            ['Demir, çinko ve iyot nasıl planlanır?', '<p>Bitkisel demirin emilimi hayvansal kaynaklardaki hem demire göre daha değişkendir. Baklagil, tahıl, kuruyemiş ve tohumlarla birlikte C vitamini içeren sebze veya meyve tüketmek emilimi destekleyebilir. Çay ve kahvenin demirden zengin ana öğünlerle birlikte aşırı tüketimi emilimi azaltabilir.</p><p>İyot için iyotlu tuz kullanımı ve toplam tuz tüketiminin dengesi değerlendirilir. Deniz yosunlarının iyot içeriği çok değişken olabildiği için “doğal olduğu için sınırsız” yaklaşımı güvenli değildir.</p>'],
            ['Kalsiyum, D vitamini ve omega-3', '<p>Kalsiyum; kalsiyumla zenginleştirilmiş bitkisel içecekler, tofu, susam/tahin ve bazı yeşil sebzelerden alınabilir. D vitamini açısından güneş maruziyeti, besinler ve gerektiğinde laboratuvarla desteklenen takviye planı değerlendirilir.</p><p>ALA için keten tohumu, chia ve ceviz kullanılabilir; EPA/DHA gereksinimi ve alg bazlı takviyeler kişisel duruma göre ele alınabilir.</p>'],
            ['Özel dönemlerde daha yakın takip gerekir', '<p>Gebelik, emzirme, çocukluk, ergenlik, ileri yaş ve yoğun spor dönemlerinde enerji ve besin öğesi gereksinimleri değişir. Vegan veya çok kısıtlı vejetaryen beslenen bireylerde B12 başta olmak üzere demir, iyot, D vitamini, kalsiyum ve protein yeterliliği daha dikkatli izlenmelidir.</p><p>Gerektiğinde hekim tarafından istenen laboratuvar sonuçları beslenme planının güvenli biçimde kişiselleştirilmesine yardımcı olur.</p>']
        ]
    })

services_path.write_text(json.dumps(services, ensure_ascii=False, indent=2) + '\n')

build = build_path.read_text()
build = build.replace("'url':'/hizmetler/saglikli-beslenme/'},\n    {'icon':'🦋','title':'Haşimato Diyeti'", "'url':'/hizmetler/vejetaryen-vegan-beslenme/'},\n    {'icon':'🦋','title':'Haşimato Diyeti'")
build_path.write_text(build)

site = json.loads(site_path.read_text())
page_updates = site.setdefault('page_updates', {})
for route in [
    '/hizmetler/kilo-verme/',
    '/hizmetler/kilo-alma/',
    '/hizmetler/sporcu-beslenmesi/',
    '/hizmetler/gebelik-emzirme-beslenmesi/',
    '/hizmetler/vejetaryen-vegan-beslenme/'
]:
    page_updates[route] = '2026-09-09'
site['updated'] = '2026-09-09'
site_path.write_text(json.dumps(site, ensure_ascii=False, indent=2) + '\n')

print('Refined service science batch 2 complete.')
