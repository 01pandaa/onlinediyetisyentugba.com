from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
build_path = ROOT / 'scripts' / 'build.py'
app_path = ROOT / 'assets' / 'app.js'
polish_path = ROOT / 'assets' / 'polish.css'

text = build_path.read_text(encoding='utf-8')

if "'tugba-hero-orijinal.svg':(1000,928)" not in text:
    needle = "'tugba-doga-yakin.webp':(750,1000)}"
    if needle not in text:
        raise SystemExit('Could not find image dimension map anchor')
    text = text.replace(needle, "'tugba-doga-yakin.webp':(750,1000),'tugba-hero-orijinal.svg':(1000,928)}", 1)

new_hero = r"""    body=f'''<section class="hero home-hero" aria-labelledby="home-title"><div class="wrap hero-grid"><div class="hero-copy">{eyebrow('DİYETİSYEN TUĞBA ŞEKER AĞAÇ')}<h1 id="home-title"><span class="headline-main">Online diyetisyen ile</span><span class="accent">kendine iyi bak.</span></h1><p class="lead">Yasaksız, sürdürülebilir ve kişiye özel beslenme listeleriyle; günlük hayatına ve sevdiğin yemeklere uygun bir düzeni birlikte oluşturalım.</p><div class="hero-actions">{link(WA,'<span class="hero-cta-icon" aria-hidden="true">✆</span><span>Ücretsiz bilgi almak istiyorum</span><span class="hero-cta-arrow" aria-hidden="true">→</span>','hero-cta hero-cta-primary',True)}{link(WA,'<span class="hero-cta-icon phone" aria-hidden="true">☎</span><span>'+e(S['phone_display'])+'</span>','hero-cta hero-cta-secondary',True)}</div><ul class="hero-benefits" aria-label="Danışmanlık yaklaşımı"><li><span class="benefit-check" aria-hidden="true">✓</span><span>Kişiye özel program</span></li><li><span class="benefit-check" aria-hidden="true">✓</span><span>Düzenli takip &amp; destek</span></li><li><span class="benefit-check" aria-hidden="true">✓</span><span>Yasaksız beslenme</span></li></ul></div><figure class="hero-photo hero-photo-original">{img('tugba-hero-orijinal.svg','Diyetisyen Tuğba Şeker Ağaç beyaz önlüğüyle dış mekânda','hero-portrait-original',eager=True)}<div class="hero-photo-note" aria-hidden="true">Daha sağlıklı,<br>daha mutlu <strong>sen.</strong> ♡</div><figcaption class="photo-caption"><span>DİYETİSYEN</span><strong>Tuğba Şeker Ağaç</strong><span>Erciyes Üniversitesi · Beslenme ve Diyetetik</span></figcaption></figure></div></section>
    <div class="intro-band">'''
"""

pattern = re.compile(r"    body=f'''<section class=\"hero home-hero\".*?</section>\n    <div class=\"intro-band\">", re.S)
text, count = pattern.subn(new_hero, text, count=1)
if count != 1:
    raise SystemExit(f'Homepage hero replacement count was {count}')

text = text.replace("/assets/app.js')}?v=mobile-header-v2", "/assets/app.js')}?v=hero-original-v6", 1)
build_path.write_text(text, encoding='utf-8')

app = app_path.read_text(encoding='utf-8')
app = app.replace('/assets/polish.css?v=home-hero-v1', '/assets/polish.css?v=hero-original-v6')
app_path.write_text(app, encoding='utf-8')

css = r'''@charset "UTF-8";

/* Homepage hero — exact user photo, no AI crop, premium conversion layout */
.home-hero{
  position:relative;
  overflow:hidden;
  background:
    radial-gradient(circle at 8% 20%,rgba(219,239,202,.68),transparent 30rem),
    radial-gradient(circle at 93% 7%,rgba(237,228,205,.8),transparent 25rem),
    linear-gradient(110deg,#fbfaf5 0%,#f8f7f0 52%,#f2f7ee 100%);
  border-bottom:1px solid #dbe4d9;
}
.home-hero::before{
  content:"";
  position:absolute;
  width:560px;
  height:560px;
  right:-170px;
  bottom:-310px;
  border-radius:50%;
  border:1px solid rgba(37,103,72,.12);
  box-shadow:0 0 0 58px rgba(37,103,72,.024),0 0 0 116px rgba(37,103,72,.017);
  pointer-events:none;
}
.home-hero .hero-grid{
  display:grid;
  grid-template-columns:minmax(0,1.08fr) minmax(420px,.92fr);
  align-items:center;
  gap:76px;
  min-height:710px;
  padding:72px 0 94px;
}
.home-hero .hero-copy{position:relative;z-index:3;max-width:720px}
.home-hero .eyebrow{
  display:inline-flex;
  align-items:center;
  gap:9px;
  margin-bottom:28px;
  padding:9px 14px;
  border:1px solid rgba(35,103,70,.19);
  border-radius:999px;
  background:rgba(255,255,255,.65);
  color:#315f49;
  font-size:10px;
  font-weight:800;
  letter-spacing:.15em;
  backdrop-filter:blur(8px);
}
.home-hero .eyebrow::before{
  content:"";
  width:8px;
  height:8px;
  border-radius:50%;
  background:#62a45d;
  box-shadow:0 0 0 4px rgba(98,164,93,.13);
}
.home-hero h1{
  max-width:760px;
  margin:0 0 28px;
  color:#173d31;
  font-size:clamp(56px,5.7vw,86px);
  font-weight:850;
  line-height:.97;
  letter-spacing:-.055em;
}
.home-hero h1 .headline-main{display:block;font-weight:850}
.home-hero h1 .accent{
  display:block;
  margin-top:5px;
  color:#4d8858;
  font-family:Georgia,"Times New Roman",serif;
  font-style:italic;
  font-weight:700;
  letter-spacing:-.045em;
}
.home-hero .lead{
  max-width:640px;
  color:#536960;
  font-size:19px;
  line-height:1.7;
}
.home-hero .hero-actions{
  display:flex;
  align-items:stretch;
  flex-wrap:wrap;
  gap:14px;
  margin-top:34px;
}
.home-hero .hero-cta{
  min-height:58px;
  display:inline-flex;
  align-items:center;
  justify-content:center;
  gap:11px;
  padding:15px 22px;
  border-radius:14px;
  font-size:15px;
  font-weight:800;
  line-height:1.2;
  text-decoration:none;
  transition:transform .18s ease,box-shadow .18s ease,background .18s ease,border-color .18s ease;
}
.home-hero .hero-cta:hover{transform:translateY(-2px)}
.home-hero .hero-cta:focus-visible{outline:3px solid rgba(37,211,102,.28);outline-offset:3px}
.home-hero .hero-cta-primary{
  min-width:335px;
  color:#fff;
  background:#25D366;
  border:1px solid #25D366;
  box-shadow:0 15px 30px rgba(37,211,102,.24);
}
.home-hero .hero-cta-primary:hover{background:#20c85e;border-color:#20c85e;box-shadow:0 17px 34px rgba(37,211,102,.3)}
.home-hero .hero-cta-secondary{
  min-width:210px;
  color:#174a36;
  background:rgba(255,255,255,.86);
  border:1px solid #c8d8ce;
  box-shadow:0 12px 28px rgba(38,79,57,.07);
}
.home-hero .hero-cta-secondary:hover{background:#fff;border-color:#9fc2ab}
.home-hero .hero-cta-icon{font-size:25px;line-height:1}
.home-hero .hero-cta-icon.phone{color:#159447;font-size:23px}
.home-hero .hero-cta-arrow{margin-left:auto;font-size:19px}
.home-hero .hero-benefits{
  display:flex;
  align-items:center;
  flex-wrap:wrap;
  gap:0;
  margin:38px 0 0;
  padding:0;
  list-style:none;
}
.home-hero .hero-benefits li{
  display:flex;
  align-items:center;
  gap:10px;
  padding:7px 22px;
  color:#183f31;
  font-size:14px;
  font-weight:750;
  white-space:nowrap;
}
.home-hero .hero-benefits li:first-child{padding-left:0}
.home-hero .hero-benefits li+li{border-left:1px solid #d8e2da}
.home-hero .benefit-check{
  display:grid;
  place-items:center;
  width:28px;
  height:28px;
  flex:0 0 28px;
  border-radius:50%;
  background:#e8f5e9;
  color:#159447;
  font-size:16px;
  font-weight:900;
}
.home-hero .hero-photo{
  position:relative;
  isolation:isolate;
  margin:0 0 18px;
  padding:14px;
  border:1px solid rgba(72,126,87,.2);
  border-radius:48px 48px 48px 145px;
  background:rgba(255,255,255,.68);
  box-shadow:0 30px 70px rgba(24,57,46,.14);
}
.home-hero .hero-photo::before{
  content:"";
  position:absolute;
  z-index:-2;
  inset:-30px -30px -38px 28px;
  border-radius:52% 42% 50% 46%;
  background:rgba(214,235,199,.48);
  border:1px solid rgba(74,129,88,.14);
}
.home-hero .hero-photo::after{
  content:"";
  position:absolute;
  z-index:-1;
  width:150px;
  height:220px;
  right:-45px;
  bottom:30px;
  border-radius:70% 30% 68% 32%;
  background:rgba(190,222,176,.34);
  transform:rotate(15deg);
}
.home-hero .hero-photo>img{
  display:block;
  width:100%;
  height:auto;
  aspect-ratio:auto;
  object-fit:contain;
  object-position:center;
  border:0;
  border-radius:35px 35px 35px 126px;
  background:#eef5e9;
  box-shadow:none;
}
.home-hero .hero-photo-note{
  position:absolute;
  z-index:4;
  right:-32px;
  top:74px;
  display:grid;
  place-items:center;
  width:142px;
  min-height:142px;
  padding:20px;
  border:1px solid rgba(65,116,76,.14);
  border-radius:50%;
  background:rgba(255,253,246,.94);
  color:#4b7656;
  box-shadow:0 16px 38px rgba(24,57,46,.1);
  font-family:Georgia,"Times New Roman",serif;
  font-size:16px;
  font-style:italic;
  line-height:1.28;
  text-align:center;
}
.home-hero .hero-photo-note strong{color:#275f3d;font-size:18px}
.home-hero .photo-caption{
  position:absolute;
  z-index:5;
  left:34px;
  right:34px;
  bottom:-42px;
  display:grid;
  gap:2px;
  min-width:0;
  padding:16px 20px;
  border:1px solid rgba(151,174,157,.35);
  border-radius:18px;
  background:rgba(255,255,255,.94);
  box-shadow:0 20px 46px rgba(24,57,46,.14);
  backdrop-filter:blur(12px);
}
.home-hero .photo-caption>span:first-child{color:#718078;font-size:9px;font-weight:800;letter-spacing:.16em}
.home-hero .photo-caption strong{color:#1f4334;font-family:Georgia,"Times New Roman",serif;font-size:24px;line-height:1.2}
.home-hero .photo-caption>span:last-child{color:#718078;font-size:10px}

.intro-band{padding:24px 0;background:#fffdf8;border-bottom:1px solid #e0e7de}
.intro-band .wrap{gap:38px}
.intro-band p{color:#28483a;font-size:22px;line-height:1.35}
.intro-band .text-link{white-space:nowrap;color:#4d6d5c}

@media (max-width:1120px){
  .home-hero .hero-grid{grid-template-columns:minmax(0,1fr) 420px;gap:44px}
  .home-hero h1{font-size:clamp(52px,5.6vw,72px)}
  .home-hero .hero-cta-primary{min-width:300px}
  .home-hero .hero-benefits li{padding-left:14px;padding-right:14px;font-size:13px}
  .home-hero .hero-photo-note{right:-20px;width:126px;min-height:126px;font-size:14px}
}
@media (max-width:860px){
  .home-hero .hero-grid{grid-template-columns:1fr;gap:58px;padding:54px 0 104px}
  .home-hero .hero-copy{max-width:none}
  .home-hero h1{font-size:clamp(48px,11vw,72px)}
  .home-hero .lead{max-width:680px}
  .home-hero .hero-photo{width:min(600px,94%);margin:0 auto}
  .home-hero .hero-photo-note{right:-18px}
}
@media (max-width:620px){
  .home-hero .hero-grid{padding-top:40px;gap:46px}
  .home-hero .eyebrow{margin-bottom:21px}
  .home-hero h1{font-size:clamp(43px,13vw,58px);line-height:1}
  .home-hero .lead{font-size:16px;line-height:1.68}
  .home-hero .hero-actions{display:grid;grid-template-columns:1fr}
  .home-hero .hero-cta,.home-hero .hero-cta-primary,.home-hero .hero-cta-secondary{width:100%;min-width:0}
  .home-hero .hero-benefits{display:grid;grid-template-columns:1fr;gap:10px;margin-top:30px}
  .home-hero .hero-benefits li,.home-hero .hero-benefits li:first-child{padding:0;border:0}
  .home-hero .hero-photo{width:100%;padding:10px;border-radius:36px 36px 36px 100px}
  .home-hero .hero-photo>img{border-radius:28px 28px 28px 88px}
  .home-hero .hero-photo-note{display:none}
  .home-hero .photo-caption{left:18px;right:18px;bottom:-46px;padding:14px 16px}
  .intro-band .wrap{align-items:flex-start;flex-direction:column;gap:12px}
  .intro-band .text-link{white-space:normal}
  .intro-band p{font-size:19px}
}
'''
polish_path.write_text(css, encoding='utf-8')

print('Homepage hero updated with original portrait, WhatsApp CTAs and benefit row.')
