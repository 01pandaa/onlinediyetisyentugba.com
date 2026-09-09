#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
services_path = ROOT / 'content' / 'services.json'
build_path = ROOT / 'scripts' / 'build.py'

updates = {
    'insulin-direncinde-beslenme': {
        'intro': 'İnsülin direncinde beslenme yalnızca şekeri azaltmakla sınırlı değildir. Öğün düzeni, karbonhidratın türü ve porsiyonu, lif ve protein dengesi, fiziksel aktivite, uyku, vücut ağırlığı ve varsa hekim tedavisi birlikte değerlendirilir. Amaç kısa süreli yasaklar yerine insülin duyarlılığını ve metabolik sağlığı destekleyen sürdürülebilir bir yaşam düzeni oluşturmaktır.',
        'sections': [
            ['İnsülin direnci nedir ve beslenmeyle ilişkisi nasıldır?', '<p>İnsülin direnci, hücrelerin insülin hormonunun etkisine verdiği yanıtın azalmasıyla ilişkilidir. Bu durumda pankreas kan şekerini dengede tutabilmek için daha fazla insülin salgılayabilir. Beslenme tedavisinde temel hedef; kan şekeri dalgalanmalarını azaltmak, öğünlerin tokluk süresini artırmak ve toplam enerji dengesini kişiye göre düzenlemektir.</p><p>Tek bir besin, takviye veya “insülin direnci diyeti” herkeste aynı sonucu vermez. Kişinin vücut ağırlığı, kas kütlesi, hareket düzeyi, uyku süresi ve eşlik eden sağlık durumları planlamada önemlidir.</p>'],
            ['Karbonhidrat kalitesi, lif ve protein dengesi', '<p>Karbonhidrat tamamen kesilmek zorunda değildir. Tam tahıllar, baklagiller, sebzeler ve meyveler gibi liften zengin kaynakların uygun porsiyonlarda kullanılması; rafine karbonhidratların ve yüksek oranda işlenmiş ürünlerin sıklığının azaltılması metabolik açıdan daha dengeli bir öğün yapısına katkı sağlayabilir.</p><p>Protein ve lif içeren öğünler tokluk süresini destekleyebilir. Öğün içeriği kişisel gereksinime göre düzenlenir; herkese aynı karbonhidrat miktarı veya aynı öğün sayısı önerilmez.</p>'],
            ['Kilo yönetimi ve fiziksel aktivitenin rolü', '<p>Fazla kilo varsa mütevazı ve sürdürülebilir kilo kaybı insülin duyarlılığını olumlu etkileyebilir. Ancak normal kiloda olup insülin direnci bulunan bireylerde hedef her zaman kilo vermek değildir.</p><p>Düzenli fiziksel aktivite, özellikle aerobik hareket ile direnç egzersizlerinin birlikte kullanılması, kas dokusunun glukoz kullanımını destekleyebilir. Beslenme ve hareket planı birlikte ele alındığında metabolik sonuçlar daha güçlü olabilir.</p>'],
            ['Takipte hangi göstergeler değerlendirilir?', '<p>Öğünlerin uygulanabilirliği, açlık-tokluk durumu, bel çevresi veya vücut ağırlığındaki değişim ve hekim tarafından takip edilen açlık glukozu, HbA1c, insülin veya lipid profili gibi tetkikler birlikte değerlendirilebilir. Laboratuvar sonuçları tek başına diyetisyenin tanı koyması veya ilaç dozunu değiştirmesi için kullanılmaz.</p>']
        ]
    },
    'pcos-beslenmesi': {
        'intro': 'Polikistik Over Sendromu (PCOS) heterojen bir durumdur; her bireyde insülin direnci, kilo artışı veya aynı hormonal bulgular görülmez. Beslenme yaklaşımı kişinin metabolik durumu, adet düzeni, hekim tedavisi, kilo hedefi, yaşam biçimi ve yeme davranışı dikkate alınarak kişiselleştirilir.',
        'sections': [
            ['PCOS’ta beslenme yaklaşımının temel amacı', '<p>PCOS için bilimsel olarak kanıtlanmış tek bir “mucize diyet” yoktur. Güncel yaklaşım; beslenme kalitesini artırmak, metabolik riskleri azaltmak ve uygulanabilir yaşam tarzı değişiklikleri oluşturmaktır.</p><p>Kilo kaybı gereksinimi varsa küçük ve sürdürülebilir değişiklikler bile metabolik göstergeler açısından yarar sağlayabilir. Normal kilolu bireylerde ise yalnızca kilo odaklı bir yaklaşım doğru değildir.</p>'],
            ['İnsülin direnci ve öğün yapısı', '<p>PCOS’ta insülin direnci sık görülebilir ancak herkeste bulunmaz. Liften zengin karbonhidrat kaynakları, yeterli protein, sebze ağırlığı ve uygun yağ kaynaklarıyla dengelenmiş öğünler kan şekeri kontrolünü destekleyebilir.</p><p>Karbonhidratın tamamen kesilmesi veya uzun süreli aşırı kısıtlama şart değildir. Plan kişisel tolerans, fiziksel aktivite ve toplam enerji gereksinimine göre düzenlenir.</p>'],
            ['Yağ kalitesi ve kardiyometabolik sağlık', '<p>PCOS; dislipidemi, tip 2 diyabet ve kardiyometabolik risklerle ilişkili olabilir. Bu nedenle zeytinyağı, yağlı tohumlar, balık gibi doymamış yağ kaynaklarının dengeli kullanılması; aşırı işlenmiş gıdaların ve doymuş yağın azaltılması genel sağlık açısından önem taşır.</p>'],
            ['Takviyeler konusunda neden dikkatli olunmalı?', '<p>D vitamini, inositol ve benzeri takviyelerle ilgili çalışmalar bulunmakla birlikte sonuçlar kişiden kişiye değişir ve kanıt düzeyi her ürün için aynı değildir. Takviye kullanımı laboratuvar sonuçları, kullanılan ilaçlar ve hekim önerileriyle birlikte değerlendirilmelidir.</p>']
        ]
    },
    'hasimato-diyeti': {
        'intro': 'Haşimato tiroiditinde beslenme, tiroid hormon replasmanının yerine geçmez. Amaç; yeterli enerji ve protein alımını sağlamak, micronutrient yetersizliklerini önlemek, varsa çölyak gibi eşlik eden durumları dikkate almak ve gereksiz kısıtlamalardan kaçınan dengeli bir beslenme düzeni oluşturmaktır.',
        'sections': [
            ['Haşimato için özel bir diyet var mı?', '<p>Mevcut bilimsel veriler Haşimato tiroiditini tedavi eden tek bir standart diyet göstermemektedir. Beslenme desteği; genel diyet kalitesi, vücut ağırlığı yönetimi gerekiyorsa enerji dengesi ve kişisel besin toleransı üzerinden planlanır.</p><p>Tiroid hormon tedavisi hekim tarafından düzenlenir; diyetisyen ilaç dozuna müdahale etmez.</p>'],
            ['Glutensiz beslenme herkese gerekli mi?', '<p>Çölyak hastalığı veya doğrulanmış glutenle ilişkili bir durum yoksa Haşimato tanısı olan herkese rutin glutensiz diyet önerilmesini destekleyen yeterli kanıt yoktur. Gereksiz gluten kısıtlaması lif, B vitaminleri ve besin çeşitliliğini azaltabilir.</p><p>Çölyak şüphesi varsa gluteni kendi kendine kesmeden önce hekim değerlendirmesi önemlidir; aksi halde tanısal testler etkilenebilir.</p>'],
            ['İyot, selenyum, demir ve D vitamini', '<p>Tiroid fonksiyonu için iyot, selenyum ve demir gibi mikrobesinler önemlidir; ancak “fazlası daha iyidir” yaklaşımı doğru değildir. Özellikle aşırı iyot alımı bazı tiroid hastalıklarında olumsuz olabilir.</p><p>Selenyum veya D vitamini takviyesi rutin olarak herkese başlanmamalı; yetersizlik, beslenme durumu ve hekim değerlendirmesi dikkate alınmalıdır.</p>'],
            ['Tiroid ilacı ve besin etkileşimleri', '<p>Levotiroksin gibi tiroid ilaçlarının emilimi; yemek zamanı, kahve, kalsiyum ve demir içeren takviyelerden etkilenebilir. İlacın kullanım şekli reçeteyi düzenleyen hekimin önerisine göre sürdürülmeli, beslenme planı bu zamanlamaya uyarlanmalıdır.</p>']
        ]
    },
    'lipodem-diyeti': {
        'intro': 'Lipödem kronik bir yağ dokusu hastalığıdır ve yalnızca diyetle ortadan kaldırılan bir durum değildir. Beslenme desteğinin amacı; eşlik eden fazla kiloyu yönetmek, metabolik sağlığı desteklemek, yeterli beslenmeyi sürdürmek ve günlük yaşamı kolaylaştırmaktır. Yaklaşım multidisipliner tedavinin bir parçası olmalıdır.',
        'sections': [
            ['Lipödemde beslenmenin bilimsel rolü', '<p>Lipödem dokusunu tamamen ortadan kaldırdığı kanıtlanmış özel bir diyet bulunmamaktadır. Bununla birlikte fazla kilo ve metabolik bozukluklar belirtilerin yönetimini zorlaştırabileceği için sağlıklı vücut ağırlığı ve dengeli beslenme önemlidir.</p><p>Beslenme tedavisi; ağrı, hareket kapasitesi, yeme davranışı ve eşlik eden hastalıklar dikkate alınarak kişiselleştirilir.</p>'],
            ['Akdeniz tipi beslenme ve işlenmiş gıdalar', '<p>Sebze, meyve, baklagil, tam tahıl, zeytinyağı, balık ve yağlı tohumlardan zengin Akdeniz tipi beslenme genel kardiyometabolik sağlık açısından güçlü kanıta sahiptir. Lipödemde de inflamasyonla ilişkili belirteçler açısından umut verici bulgular vardır; ancak bu veriler henüz kesin tedavi kanıtı değildir.</p><p>Ultra işlenmiş ürünlerin sık tüketimini azaltmak, toplam beslenme kalitesini artırmak açısından daha güvenli ve sürdürülebilir bir yaklaşımdır.</p>'],
            ['Düşük karbonhidrat veya ketojenik diyet şart mı?', '<p>Lipödemde düşük karbonhidratlı veya ketojenik diyetlerle ilgili çalışmalar artmaktadır. Bazı çalışmalarda kilo, ağrı veya vücut kompozisyonunda iyileşmeler bildirilse de uzun dönem güvenlik ve üstünlük konusunda kanıt sınırlıdır.</p><p>Bu nedenle ketojenik diyet “her lipödem hastasına gerekli” şeklinde sunulmamalı; kişinin sağlık durumu ve sürdürülebilirliği dikkate alınmalıdır.</p>'],
            ['Ödem, sıvı ve tuz yönetimi', '<p>Yeterli sıvı alımı ve sodyum tüketiminin kişinin sağlık durumuna göre değerlendirilmesi önemlidir. Hızlı sıvı kaybı vadeden detokslar, diüretik bitki karışımları veya aşırı tuz kısıtlaması bilimsel bir lipödem tedavisi değildir.</p>']
        ]
    },
    'menopozda-beslenme': {
        'intro': 'Menopoz döneminde östrojen düzeylerindeki değişim; yağ dağılımı, kas kütlesi, kemik sağlığı ve kardiyometabolik riskler üzerinde etkili olabilir. Beslenme planı yalnızca kilo vermeye değil, kas ve kemik dokusunu korumaya, yeterli protein ve mikrobesin alımına ve kalp sağlığını destekleyen uzun vadeli alışkanlıklara odaklanır.',
        'sections': [
            ['Vücut kompozisyonu neden değişebilir?', '<p>Menopoz geçişinde karın çevresinde yağlanma artabilir ve yaşla birlikte yağsız vücut kütlesi azalabilir. Tartıdaki kilo çok değişmese bile vücut kompozisyonu değişebilir.</p><p>Bu nedenle değerlendirmede yalnızca kilogram değil; bel çevresi, kas kütlesi, hareket düzeyi ve günlük protein dağılımı da önem taşır.</p>'],
            ['Protein ve kas dokusunu koruma', '<p>Yeterli protein alımı ve proteinin gün içine dengeli dağıtılması, özellikle direnç egzersiziyle birlikte kas dokusunun korunmasını destekler. Gereksinim yaş, vücut ağırlığı, böbrek sağlığı ve aktivite düzeyine göre kişiselleştirilir.</p>'],
            ['Kalsiyum, D vitamini ve kemik sağlığı', '<p>Menopoz sonrası kemik kaybı riski artar. Süt ve süt ürünleri veya uygun alternatifler, yeşil yapraklı sebzeler ve diğer kalsiyum kaynakları beslenmede değerlendirilir. D vitamini gereksinimi ise kan düzeyi, güneş maruziyeti ve hekim değerlendirmesine göre ele alınır.</p>'],
            ['Kalp sağlığı ve beslenme modeli', '<p>Akdeniz tipi beslenme; sebze, meyve, tam tahıl, baklagil, zeytinyağı, balık ve kuruyemişlerden zengin yapısıyla kalp-damar ve metabolik sağlık açısından güçlü bir seçenektir. Menopozda beslenme planı bu ilkeler temelinde kişiselleştirilebilir.</p><p>Sıcak basması gibi belirtilerde tek bir besinin kesin tedavi etkisi gösterilmemiştir; kişisel tetikleyiciler ayrıca değerlendirilebilir.</p>']
        ]
    },
    'emzirme-doneminde-beslenme': {
        'intro': 'Emzirme döneminde beslenme; annenin artan enerji ve besin öğesi gereksinimlerini karşılamayı, toparlanmayı desteklemeyi ve süt üretimini sürdürebilecek yeterli bir beslenme düzeni oluşturmayı amaçlar. Katı yasaklar veya hızlı kilo kaybı programları yerine besin çeşitliliği ve yeterlilik ön plandadır.',
        'sections': [
            ['Enerji gereksinimi neden artar?', '<p>Süt üretimi enerji gerektiren bir süreçtir. Ancak ihtiyaç; annenin vücut ağırlığı, gebelikte aldığı kilo, günlük hareketi, emzirme sıklığı ve doğum sonrası döneme göre değişir. Her emziren anneye aynı kalori düzeyi uygun değildir.</p><p>Çok düşük kalorili diyetler yorgunluğu artırabilir ve besin öğesi yeterliliğini zorlaştırabilir.</p>'],
            ['Protein, sıvı ve besin çeşitliliği', '<p>Yeterli protein; yumurta, et, balık, süt ürünleri, baklagiller veya uygun bitkisel alternatiflerle sağlanabilir. Susama hissine göre düzenli sıvı tüketmek önemlidir; aşırı su içmenin süt miktarını otomatik artırdığı gösterilmemiştir.</p><p>Emzirme döneminde tek tip beslenme yerine farklı besin gruplarını içeren çeşitli bir plan hedeflenir.</p>'],
            ['İyot, B12, D vitamini ve omega-3', '<p>Anne beslenmesi bazı mikrobesinlerin anne sütündeki düzeyini etkileyebilir. İyot, B12 vitamini, D vitamini ve uzun zincirli omega-3 yağ asitleri özellikle değerlendirilmesi gereken öğelerdir.</p><p>Vegan veya çok kısıtlı beslenen annelerde B12 başta olmak üzere bazı eksiklik riskleri artabilir. Takviyeler kişisel durum ve hekim önerisiyle planlanmalıdır.</p>'],
            ['Emzirirken kilo verme', '<p>Doğum sonrası kilo kaybı hedefleniyorsa hızlı ve agresif kısıtlamalar yerine kademeli bir yaklaşım daha uygundur. Beslenme planı annenin açlık düzeyi, uyku durumu, süt üretimi ve genel sağlık hali dikkate alınarak düzenlenir.</p>']
        ]
    },
    'diyabet-beslenmesi': {
        'intro': 'Diyabette tıbbi beslenme tedavisi; kan şekeri kontrolünü desteklemek, kardiyometabolik riski azaltmak ve bireyin günlük yaşamına uyarlanabilen bir beslenme düzeni oluşturmak amacıyla kişiselleştirilir. İlaç ve insülin tedavisiyle uyum, öğün zamanlaması ve hipoglisemi riski mutlaka dikkate alınır.',
        'sections': [
            ['Diyabette tek bir doğru diyet var mı?', '<p>Tip 1 veya tip 2 diyabet için herkesin uygulaması gereken tek bir makro besin dağılımı yoktur. Karbonhidrat, protein ve yağ oranları; kişinin tedavisi, yeme alışkanlıkları, kilo hedefi ve metabolik durumuna göre düzenlenir.</p><p>Tıbbi beslenme tedavisinin diyetisyen tarafından bireyselleştirilmesi, glisemik ve kardiyometabolik sonuçları iyileştirebilir.</p>'],
            ['Karbonhidrat miktarı kadar kalitesi de önemlidir', '<p>Tam tahıl, baklagil, sebze ve meyve gibi lif içeren karbonhidrat kaynakları; rafine tahıllar ve şekerli içeceklere göre daha dengeli seçeneklerdir. Karbonhidratın öğünlere dağılımı kullanılan ilaç veya insülin tedavisine göre planlanabilir.</p>'],
            ['Protein, yağ ve kalp sağlığı', '<p>Diyabet kalp-damar hastalığı riskini artırabildiği için yağ kalitesi önemlidir. Zeytinyağı, balık, kuruyemiş ve tohumlar gibi doymamış yağ kaynakları önceliklendirilebilir; doymuş yağ ve ultra işlenmiş ürünlerin sıklığı azaltılabilir.</p>'],
            ['Hipoglisemi ve ilaç uyumu', '<p>İnsülin veya hipoglisemi riski oluşturan ilaç kullanan bireylerde öğün düzenini ani biçimde değiştirmek risk yaratabilir. Açlık, egzersiz ve karbonhidrat miktarındaki değişiklikler sağlık ekibiyle uyumlu planlanmalıdır. Diyetisyen ilaç dozunu değiştirmez.</p>']
        ]
    },
    'eliminasyon-diyeti': {
        'intro': 'Eliminasyon diyeti, belirli bir besin veya besin grubunun semptomlarla ilişkisini değerlendirmek amacıyla geçici ve planlı olarak uygulanır. Bilimsel yaklaşım; gereksiz yasaklardan kaçınmak, kısıtlama süresini sınırlamak, besin yeterliliğini korumak ve uygun zamanda kontrollü yeniden deneme yapmaktır.',
        'sections': [
            ['Eliminasyon diyeti ne zaman düşünülür?', '<p>Eliminasyon yaklaşımı; doğrulanmış alerji, intolerans, çölyak gibi tıbbi durumlarda veya belirli gastrointestinal yakınmalarda hekim ve diyetisyen değerlendirmesiyle kullanılabilir. Rastgele çok sayıda besini aynı anda çıkarmak neden-sonuç ilişkisini anlamayı zorlaştırır.</p>'],
            ['Kısıtlama aşaması neden geçici olmalıdır?', '<p>Uzun süreli ve geniş kapsamlı kısıtlamalar enerji, protein, lif, vitamin ve mineral alımını azaltabilir. Ayrıca sosyal yaşamı ve yeme davranışını olumsuz etkileyebilir. Bu nedenle eliminasyonun amacı mümkün olduğunca az kısıtlamayla semptom kontrolünü sağlamaktır.</p>'],
            ['Yeniden deneme ve kişiselleştirme', '<p>Örneğin düşük FODMAP yaklaşımında bilimsel uygulama yalnızca kısıtlama aşamasından oluşmaz; yeniden deneme ve kişiselleştirme aşamaları da sürecin temel parçasıdır. Tolere edilen besinlerin yeniden diyete eklenmesi beslenme çeşitliliğini artırır.</p>'],
            ['IgG gıda testleri neden tek başına yeterli değildir?', '<p>Semptomlara neden olan besinleri belirlemek için ticari IgG gıda panellerinin rutin kullanımını destekleyen güçlü klinik kanıt yoktur. Eliminasyon kararı sağlık öyküsü, semptom kaydı ve gerektiğinde tıbbi tanı süreciyle verilmelidir.</p>']
        ]
    },
    'glutensiz-beslenme': {
        'intro': 'Glutensiz beslenme çölyak hastalığında yaşam boyu tedavinin temelidir. Bunun dışında glutenin çıkarılması ancak tıbbi gerekçe olduğunda planlanmalıdır. Amaç yalnızca gluteni kesmek değil, besin yeterliliğini ve lif alımını koruyan dengeli bir glutensiz düzen oluşturmaktır.',
        'sections': [
            ['Çölyak hastalığında neden tamamen glutensiz beslenilir?', '<p>Çölyak hastalığında gluten bağışıklık aracılı ince bağırsak hasarına yol açar. Bu nedenle buğday, arpa ve çavdar kaynaklı glutenin tamamen çıkarılması gerekir. Az miktarda gluten maruziyeti bile bağırsak hasarını sürdürebileceği için çapraz bulaşma konusunda eğitim önemlidir.</p>'],
            ['Glutensiz ürünler otomatik olarak daha sağlıklı değildir', '<p>Glutensiz paketli ürünlerin bazıları liften fakir, yağ veya şekerden zengin olabilir. Bu nedenle glutensiz beslenme yalnızca özel ürünlere dayanmak yerine patates, pirinç, karabuğday, kinoa, mısır, baklagil, sebze ve meyve gibi doğal olarak glutensiz kaynaklarla çeşitlendirilmelidir.</p>'],
            ['Demir, folat, B vitaminleri ve lif', '<p>Çölyak tanısı sırasında demir, folat, B12 veya D vitamini gibi eksiklikler görülebilir. Ayrıca uzun dönem glutensiz diyette lif ve bazı mikrobesinlerin yetersiz kalma riski vardır. Bu nedenle beslenme kalitesi ve gerektiğinde laboratuvar sonuçları izlenmelidir.</p>'],
            ['Gluteni kesmeden önce tanı neden önemlidir?', '<p>Çölyak şüphesi varsa glutenli beslenme tanı testleri tamamlanmadan kesilmemelidir. Glutensiz diyete erken başlamak antikor testleri ve biyopsi sonuçlarını etkileyerek tanıyı zorlaştırabilir.</p>']
        ]
    },
    'cocuk-ergen-beslenmesi': {
        'intro': 'Çocuk ve ergen beslenmesinde temel hedef yalnızca kilo kontrolü değildir; büyüme, puberte, kemik gelişimi, okul performansı ve sağlıklı yeme davranışının desteklenmesi ön plandadır. Plan; yaşa, büyüme eğrisine, aktivite düzeyine, aile düzenine ve varsa sağlık durumuna göre hazırlanır.',
        'sections': [
            ['Büyüme eğrisi neden önemlidir?', '<p>Çocuklarda kilo tek başına değerlendirilmez. Boy, kilo, yaş, cinsiyet ve zaman içindeki büyüme eğilimi birlikte incelenir. Ani kilo kaybı, büyümede duraklama veya hızlı kilo artışı varsa çocuk hekimi değerlendirmesi gerekebilir.</p>'],
            ['Enerji ve protein gereksinimi yetişkinlerden farklıdır', '<p>Çocuklar büyüme döneminde oldukları için enerji ve protein yetersizliği gelişimi etkileyebilir. Bu nedenle yetişkinlere yönelik düşük kalorili veya çok düşük karbonhidratlı diyetlerin çocuklara uyarlanması doğru değildir.</p>'],
            ['Demir, kalsiyum ve D vitamini', '<p>Ergenlik döneminde özellikle demir, kalsiyum ve D vitamini gereksinimleri önem kazanır. Adet gören ergen kızlarda demir eksikliği riski artabilir; süt ürünlerini tüketmeyen çocuklarda kalsiyum kaynakları ayrıca planlanmalıdır.</p>'],
            ['Aile temelli yaklaşım ve yeme davranışı', '<p>Sağlıklı beslenme alışkanlıklarının kalıcı olması için yalnızca çocuğa yasak koymak yerine evdeki yemek düzeni, erişilebilir besinler ve aile modeli birlikte ele alınır. Aşırı kilo odaklı dil, katı yasaklar ve sürekli tartılma çocuklarda beden algısını ve yeme davranışını olumsuz etkileyebilir.</p>']
        ]
    }
}

services = json.loads(services_path.read_text())
for service in services:
    service.pop('related', None)
    service.pop('source', None)
    data = updates.get(service.get('slug'))
    if data:
        service['intro'] = data['intro']
        service['sections'] = data['sections']
services_path.write_text(json.dumps(services, ensure_ascii=False, indent=2) + '\n')

build = build_path.read_text()
lines = build.splitlines()
lines = [line for line in lines if "content+='<h2>İlgili beslenme yazısı</h2>" not in line]
build_path.write_text('\n'.join(lines) + '\n')

print('Refined scientific service content and removed unrelated blog/source blocks.')
