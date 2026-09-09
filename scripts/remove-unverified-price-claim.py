#!/usr/bin/env python3
from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'scripts' / 'build.py'
s = p.read_text()
old = '<article class="price-card featured"><span class="price-badge">EN ÇOK TERCİH EDİLEN</span><span class="price-term">3 AYLIK ONLINE PAKET</span>'
new = '<article class="price-card"><span class="price-term">3 AYLIK ONLINE PAKET</span>'
if old not in s:
    raise SystemExit('Pricing claim marker not found')
p.write_text(s.replace(old, new, 1))
print('Removed unsupported most-preferred package claim.')
