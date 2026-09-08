# Online Diyetisyen Tuğba Şeker Ağaç

Türkiye genelinde online danışmanlığı ve Adana Seyhan ofisini anlatan, Türkçe çok sayfalı web sitesi. Üretim alan adı: https://www.onlinediyetisyentugba.com

## Yapı

- `content/site.json`: İsim, telefon, adres, sosyal hesaplar, içerik güncelleme tarihi.
- `content/services.json`: Altı danışmanlık alanı ve sayfa içerikleri.
- `content/online-consultation.json`: Online danışmanlık sayfasının kapsamı, hazırlık, takip ve görüşme bilgileri.
- `content/posts/*.json`: Yeni makale eklemek için her yazıya bir dosya.
- `scripts/build.py`: Statik HTML sayfaları, site haritası, RSS ve robots.txt üretir.
- `assets/`: Ortak tasarım, tarayıcı etkileşimleri, yerel görseller.
- `dist/`: Üretilen yayın dosyalarının geçici kopyası.
- `index.html`, sayfa klasörleri, `sitemap.xml`, `robots.txt`, `feed.xml`: GitHub Pages için depo kökünde tutulan yayın dosyaları; `build.py` ile otomatik güncellenir.
- `.generated-pages.json`: Derleyicinin yönettiği yayın dosyaları.
- `.nojekyll`: Hazır HTML dosyalarının Jekyll dönüşümü olmadan sunulmasını sağlar.

## Yerelde derleme

Python 3.12 veya üzeri; harici Python paketi gerekmez. Node.js yalnızca hesaplayıcı kontrolünde kullanılır.

```sh
python3 scripts/build.py
python3 scripts/check.py
node scripts/check-calculator.cjs
python3 -m http.server 8080 --directory dist
```

## Yeni blog yazısı ekleme

1. `content/posts/` altındaki örneklerden birini yeni adla kopyalayın.
2. `slug` için benzersiz, Türkçe karakter içermeyen, küçük harfli bir adres kullanın.
3. Başlık, özgün açıklama, kategori, gerçek yayın tarihi, giriş, görsel ve bölümleri düzenleyin.
4. `sources` alanına doğrulanmış birincil kaynaklar ekleyin. İçerikteki tıbbi bilgileri mesleki olarak gözden geçirin; incelenmeyen içeriğe “uzman onaylı” ifadesi eklemeyin.
5. `assets/images/` içine kullanım hakkı bulunan görseli ekleyip `image` ve açıklayıcı `image_alt` alanını güncelleyin. Anatomik görsellerde kaynak ve lisans atfını koruyun.
6. Yazının `date` alanı ilk yayın tarihidir; anlamlı içerik değişikliğinde o yazıya `updated` ekleyin. Hizmet veya liste sayfası değiştiğinde `content/site.json` içindeki `page_updates` alanında yalnızca ilgili yolu güncelleyin. Sırf güncel görünmek için tarih değiştirmeyin.
7. Derleme ve kontrolleri çalıştırın. `build.py`, yeni sayfayı ve tüm ilgili yayın dosyalarını depo kökünde de günceller. Kaynaklarla birlikte bu dosyaları `main` dalına gönderin. GitHub Pages yayını otomatik yeniler.

Blog listesi, kategori filtreleri, arama, ilgili yazılar, RSS, makale JSON-LD bilgileri ve sitemap otomatik oluşur. `featured: true` ana sayfada öne çıkarmak için kullanılabilir. Bölüm içerikleri güvenilir editöre ait HTML kabul eder; kullanıcıdan gönderilen HTML doğrudan eklenmemelidir.

İsteğe bağlı `seo_title`, görünür uzun makale başlığından ayrı bir arama başlığı tanımlar. `related`, ilgili yazıların mevcut slug değerlerini sıralar. `author_type: "editorial"`, yazarı site işletmesi olarak belirtir; bağımsız bir uzman incelemesi yapıldığını iddia etmez. `editorial_note`, hazırlama yöntemi ve kaynak kontrolü gibi gerçek bilgileri yazının sonunda gösterir. Kaynakların desteklediği açıklamalara içerik içinde de bağlantı verin.

## Yayın

Bu deponun mevcut GitHub Pages yayını **Deploy from a branch → main → /(root)** kaynağını kullanır. `build.py` bu konuma tam siteyi yazar. Kök `index.html` ve `.nojekyll` dosyalarını koruyun; yalnızca `README.md` bulunan bir kök dizin yayımlamayın. `publish.yml` derlemeyi, bağlantıları, hesaplayıcıyı ve kaydedilmiş yayın dosyalarının güncelliğini denetler. Ayrı bir `deploy-pages` işi çalıştırılmaz; böylece iki farklı yayın süreci birbirinin çıktısını değiştirmez.

GitHub Pages özel alan adı `www.onlinediyetisyentugba.com` olarak ayarlıdır. `CNAME` ve `content/site.json` bu tercihle aynı kalmalıdır. `www` içermeyen kök alan adı da DNS/alan adı sağlayıcısında bu adrese yönlendirilmelidir. Alan adı bilgisi `content/site.json` dosyasında tek yerden yönetilir. Eski `onlinediyetisyen.online` sitesi bu depo tarafından değiştirilmez. Taşıma yapılacaksa eski URL’ler için ayrı bir 301 eşlemesi hazırlanmalıdır.

Başka bir barındırmaya geçildiğinde `dist` içeriği web köküne aktarılabilir. Alt dizinde önizleme için `SITE_PATH_PREFIX=/onlinediyetisyentugba.com python3 scripts/build.py` kullanılabilir; üretimde önek boş olmalıdır.

## İçerik ve veri sınırları

- İletişim ve eğitim bilgileri işletmenin mevcut sitesinden alınmıştır; WhatsApp saatleri işletme sahibinin beyanıdır.
- E-posta ve X/Twitter hesabı doğrulanmadığı için eklenmemiştir.
- Google yorum sayısı ve değerlendirme metinleri yayımlanmaz. Harita konumu ve yol tarifi bağlantısı vardır. Hasta memnuniyeti üzerinden tanıtıma ilişkin güncel sınırlamalar: https://antalyaism.saglik.gov.tr/TR-366500/saglik-hizmetlerinde-tanitim-ve-bilgilendirme--faaliyetleri-hakkinda-yonetmelik.html
- Fiyat, kampanya, garanti, uydurma mesleki unvan, başarı oranı veya danışan sonucu bulunmaz.
- BKİ, yalnızca uygun yetişkinlerde genel tarama aracıdır; kişisel diyet önermez. Girdi ve sonuçlar saklanmaz veya gönderilmez.
- Sağlık bilgisi toplama formu, üyelik, analiz kodu veya reklam takip pikseli yoktur.
- YouTube ve Google Maps yalnızca kullanıcı ilgili düğmeye bastığında yüklenir; üçüncü taraf koşulları uygulanır.

## SEO takibi

Üretim alan adı doğrulandıktan sonra Search Console’da alan adını doğrulayın ve `/sitemap.xml` adresini gönderin. Ana sayfa, online danışmanlık ve ilk yazıları URL denetimiyle inceleyin. Türkiye filtresiyle tam veri içeren dönemleri karşılaştırın; son 24 saatin eksik verileri üzerinden sonuç çıkarmayın. Görünürlük hedefi teknik erişilebilirlik ve yararlı içerikle desteklenir; sıralama garantisi verilmez.

Bkz. `ASSET_CREDITS.md` ve sitedeki `/kaynaklar/` sayfası.
