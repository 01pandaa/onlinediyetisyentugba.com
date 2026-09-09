#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'scripts' / 'build.py'
s = p.read_text(encoding='utf-8')
old = "NAV=[('Ana Sayfa','/'),('Kurumsal','/kurumsal/'),('Online Diyetisyen','/online-diyetisyen/'),('Hizmetler','/hizmetler/'),('Blog','/blog/'),('SSS','/sikca-sorulan-sorular/'),('İletişim','/iletisim/')]"
new = "NAV=[('Ana Sayfa','/'),('Hakkında','/kurumsal/'),('Online Diyetisyen','/online-diyetisyen/'),('Hizmetler','/hizmetler/'),('Fiyatlar','/online-diyetisyen-fiyatlari/'),('Blog','/blog/'),('SSS','/sikca-sorulan-sorular/'),('İletişim','/iletisim/')]"
if old not in s:
    raise SystemExit('Expected NAV definition not found; no changes made.')
p.write_text(s.replace(old, new, 1), encoding='utf-8')
print('Updated main navigation order and labels.')
