#!/usr/bin/env python3
"""Strengthen the Adana local landing page without changing factual business details."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'scripts' / 'build.py'

text = BUILD.read_text()
marker = "Adana’da diyetisyen ararken nelere dikkat edebilirsiniz?"
if marker in text:
    print('Adana local SEO refinement is already applied.')
    raise SystemExit(0)

start_token = "    body=hero('Adana’da<br><span class=\"accent\">yüz yüze beslenme danışmanlığı.</span>'"
start = text.find(start_token)
if start < 0:
    raise SystemExit('Adana page start block not found')

end_token = "    layout('/adana-diyetisyen/','Adana Diyetisyen Tuğba Şeker Ağaç | Seyhan Ofisi','Adana Seyhan’da diyetisyen Tuğba Şeker Ağaç ile yüz yüze beslenme danışmanlığı. Ofis adresi, telefon, harita ve online görüşme seçeneği.',body)"
end = text.find(end_token, start)
if end < 0:
    raise SystemExit('Adana page end block not found')
end += len(end_token)

new_block = r'''    body=hero('Adana’da<br><span class="accent">yüz yüze beslenme danışmanlığı.</span>','Seyhan’daki ofiste randevulu görüşmeler. Beslenme sürecinizi günlük yaşamınız, sağlık öykünüz ve ihtiyaçlarınızla birlikte değerlendirelim. Türkiye’nin diğer şehirlerinden online katılım seçeneği de vardır.','Adana Diyetisyen','tugba-ofis-onluk.webp','portrait-cover','Diyetisyen Tuğba Şeker Ağaç Adana’daki danışmanlık ofisinde')
    local_intro="<h2>Adana’da diyetisyen ararken nelere dikkat edebilirsiniz?</h2><p>Diyetisyen seçerken yalnızca hazır bir listeye değil; sağlık öykünüzün değerlendirilmesine, günlük yaşamınıza uyarlanabilir bir plan oluşturulmasına ve sürecin düzenli takip edilmesine dikkat etmek önemlidir. Yüz yüze görüşmelerde amaç, uygulanabilir ve sürdürülebilir bir beslenme düzenini birlikte şekillendirmektir.</p><h2>Seyhan’daki ofis görüşmeleri nasıl ilerler?</h2><p>İlk görüşmede sağlık öykünüz, mevcut tanılarınız, kullandığınız ilaçlar, günlük beslenme alışkanlıklarınız, çalışma düzeniniz ve beklentileriniz ele alınır. Elinizde güncel tetkikler varsa görüşmeye getirmeniz değerlendirmeyi kolaylaştırabilir. Gerektiğinde tıbbi değerlendirme için hekiminizle görüşmeniz önerilir.</p><h2>Adana’daki günlük yaşamınıza uygun plan</h2><p>İş yerindeki öğle yemekleri, aile sofraları, dışarıda yemek, Adana mutfağındaki sevdiğiniz seçenekler ve öğün saatleriniz görüşmenin parçasıdır. Amaç yalnızca evde hazırlanabilen katı bir liste vermek değil; erişebildiğiniz ve sürdürebildiğiniz alternatifleri birlikte değerlendirmektir.</p>"
    body+=article_body(local_intro)
    body+='<section class="section soft"><div class="wrap">'+heading('GÖRÜŞME SÜRECİ','Yüz yüze beslenme danışmanlığı nasıl ilerler?','İlk değerlendirmeden takibe kadar süreç kişisel ihtiyaçlarınıza göre planlanır.')+steps()+'</div></section>'
    body+=article_body('<h2>Hangi konularda beslenme danışmanlığı alabilirsiniz?</h2><p>Yüz yüze görüşmeler; kilo yönetimi, insülin direnci, diyabet, Haşimato, PCOS, menopoz, gebelik ve emzirme dönemi, sporcu beslenmesi, çocuk ve ergen beslenmesi gibi farklı ihtiyaçlarda kişisel değerlendirmeyle planlanabilir.</p><p>'+link('/hizmetler/','Tüm beslenme danışmanlığı hizmetlerini inceleyin ↗','text-link')+'</p><h2>Online mı, yüz yüze mi?</h2><p>Adana’da yaşıyorsanız Seyhan’daki ofiste yüz yüze görüşebilirsiniz. Şehir dışında yaşıyorsanız veya ofise gelmek günlük düzeninize uygun değilse, '+link('/online-diyetisyen/','online diyetisyen danışmanlığı')+' seçeneğini inceleyebilirsiniz. Görüşme biçimi değişse de temel yaklaşım kişisel değerlendirme, planlama ve takip üzerine kuruludur.</p><h2>Ofise ulaşım ve randevu</h2><p><strong>'+e(S['address'])+'</strong></p><p>Görüşmeler randevuyla yapılır. Harita bağlantısından konumu açabilir, gelmeden önce telefon veya WhatsApp üzerinden randevu ve ofis bilgisini teyit edebilirsiniz.</p>')
    local_faq=[
        ('Adana’da yüz yüze diyetisyen görüşmesi için randevu gerekiyor mu?','Evet. Seyhan’daki ofis görüşmeleri randevuyla yapılır. Uygun gün ve saat için iletişim kanallarından bilgi alabilirsiniz.'),
        ('İlk görüşmeye kan tahlili getirmeli miyim?','Elinizde güncel tetkikler varsa görüşmeye getirmeniz değerlendirmeyi kolaylaştırabilir. Hangi tetkiklerin gerekli olduğu kişisel sağlık durumuna göre değişebilir; gerektiğinde hekim değerlendirmesi istenir.'),
        ('Adana dışında yaşayanlar da danışmanlık alabilir mi?','Evet. Türkiye’nin farklı şehirlerinden online görüşmeye katılabilirsiniz. Online süreç hakkında ayrıntılı bilgi için online diyetisyen sayfasını inceleyebilirsiniz.'),
        ('Ofis hangi bölgede?','Ofis Kurtuluş Mahallesi, Seyhan / Adana’dadır. Güncel adres ve harita bağlantısı bu sayfadaki iletişim bölümünde yer alır.')
    ]
    body+='<section class="section"><div class="wrap">'+heading('SIK SORULANLAR','Adana’daki yüz yüze görüşmeler hakkında','Randevu, ilk görüşme ve ofis konumu hakkında kısa yanıtlar.')+faqs(local_faq)+'</div></section>'
    body+='<section class="section soft"><div class="wrap stack">'+contact+map_html+'</div></section>'
    adana_service={'@type':'Service','name':'Adana yüz yüze beslenme danışmanlığı','serviceType':'Beslenme danışmanlığı','provider':{'@id':BASE+'/#kurum'},'areaServed':{'@type':'City','name':'Adana'},'url':BASE+'/adana-diyetisyen/'}
    layout('/adana-diyetisyen/','Adana Diyetisyen | Tuğba Şeker Ağaç – Seyhan Ofisi','Adana Seyhan’da diyetisyen Tuğba Şeker Ağaç ile yüz yüze beslenme danışmanlığı. Randevu süreci, ofis adresi, harita, hizmetler ve online görüşme seçeneği.',body,extra=[adana_service])'''

BUILD.write_text(text[:start] + new_block + text[end:])
print('Adana local SEO refinement applied.')
