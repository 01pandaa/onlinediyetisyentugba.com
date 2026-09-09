#!/usr/bin/env python3
"""Validate generated navigation, metadata, structured data and content sources."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from xml.etree import ElementTree as ET
import json,re
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
BASE=json.loads((ROOT/'content/site.json').read_text())['url'].rstrip('/')
errors=[];titles=set();descs=set()
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=set();self.refs=[];self.h1=0;self.meta={};self.title='';self.canonical=[];self.in_title=False;self.jsons=[];self.in_json=False;self.lang=None
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if a.get('id'):
            if a['id'] in self.ids:errors.append(f'Duplicate id {a["id"]}')
            self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='title':self.in_title=True
        if tag=='meta':self.meta[a.get('name') or a.get('property')]=a.get('content')
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
        if tag=='script' and a.get('type')=='application/ld+json':self.in_json=True;self.jsons.append('')
        if tag=='img' and (not a.get('alt') or not a.get('width') or not a.get('height')):errors.append('Image needs alt and dimensions')
        for key in ['href','src']:
            if a.get(key):self.refs.append(a[key])
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='script':self.in_json=False
    def handle_data(self,d):
        if self.in_title:self.title+=d
        if self.in_json:self.jsons[-1]+=d
pages={}
for file in OUT.rglob('*.html'):
    p=Page();p.feed(file.read_text());pages[file]=p
    if p.lang!='tr' or p.h1!=1:errors.append(f'{file}: language/H1 mismatch')
    if not p.title or p.title in titles:errors.append(f'{file}: missing/duplicate title')
    titles.add(p.title)
    description=p.meta.get('description')
    if not description or description in descs:errors.append(f'{file}: missing/duplicate description')
    descs.add(description)
    if len(p.canonical)!=1 or not p.canonical[0].startswith(BASE+'/'):errors.append(f'{file}: canonical')
    for s in p.jsons:
        try:
            graph=json.loads(s)['@graph']
            if any(x.get('@type') in ['AggregateRating','Review','Physician'] for x in graph):errors.append('Unsupported review/physician schema')
        except Exception as er:errors.append(f'{file}: invalid JSON-LD {er}')
for file,p in pages.items():
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        dest=OUT/unquote(u.path).lstrip('/') if u.path.startswith('/') else file.parent/unquote(u.path) if u.path else file
        if dest.is_dir():dest=dest/'index.html'
        if not dest.exists():errors.append(f'{file.relative_to(OUT)} -> missing {ref}')
        if u.fragment and dest in pages and unquote(u.fragment) not in pages[dest].ids:errors.append(f'{file} -> missing fragment {ref}')
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
urls=[x.text for x in ET.parse(OUT/'sitemap.xml').findall('.//s:loc',ns)]
if len(urls)!=len(set(urls)):errors.append('Duplicate sitemap URL')
for url in urls:
    route=urlsplit(url).path
    if not (OUT/route.strip('/')/'index.html').exists():errors.append('Bad sitemap URL '+url)
for f in (ROOT/'content/posts').glob('*.json'):
    p=json.loads(f.read_text())
    if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',p['slug']):errors.append('Invalid post slug '+str(f))
    if len(p['sections'])<3 or not p['sources']:errors.append('Post needs substantive sections and sources '+str(f))

# Extended technical SEO checks: exact canonicals, social metadata, sitemap completeness and orphan detection.
def page_route(file):
    rel=file.relative_to(OUT)
    if rel.as_posix()=='index.html':return '/'
    if rel.name=='index.html':return '/'+rel.parent.as_posix().strip('/')+'/'
    return '/'+rel.as_posix()

indexable={}
for file,p in pages.items():
    robots=p.meta.get('robots','') or ''
    if robots.startswith('noindex'):continue
    route=page_route(file)
    expected=BASE+route
    indexable[route]=(file,p)
    if p.canonical!=[expected]:errors.append(f'{file}: canonical must equal {expected}')
    if p.meta.get('viewport')!='width=device-width,initial-scale=1':errors.append(f'{file}: viewport')
    if robots!='index,follow,max-image-preview:large':errors.append(f'{file}: robots meta')
    for key in ['og:title','og:description','og:url','og:image']:
        if not p.meta.get(key):errors.append(f'{file}: missing {key}')
    if p.meta.get('og:url')!=expected:errors.append(f'{file}: og:url mismatch')
    if p.meta.get('og:image') and not p.meta['og:image'].startswith(BASE+'/assets/images/'):errors.append(f'{file}: og:image must be absolute')

expected_sitemap={BASE+route for route in indexable}
actual_sitemap=set(urls)
if actual_sitemap!=expected_sitemap:
    missing=sorted(expected_sitemap-actual_sitemap)
    extra=sorted(actual_sitemap-expected_sitemap)
    errors.append(f'Sitemap coverage mismatch missing={missing} extra={extra}')

incoming={route:0 for route in indexable}
for file,p in pages.items():
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc or not u.path.startswith('/'):continue
        target=unquote(u.path)
        if target in incoming:incoming[target]+=1
for route,count in incoming.items():
    if route!='/' and count==0:errors.append(f'Orphan indexable page: {route}')

robots_file=(OUT/'robots.txt').read_text()
if 'User-agent: *' not in robots_file or 'Allow: /' not in robots_file:errors.append('robots.txt basic directives')
if f'Sitemap: {BASE}/sitemap.xml' not in robots_file:errors.append('robots.txt sitemap URL')

if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(pages)} HTML pages; metadata, exact canonicals, JSON-LD, internal links, orphan detection, robots.txt and {len(urls)} sitemap URLs validated.')
for name in json.loads((ROOT/'.generated-pages.json').read_text()):
    assert (ROOT/name).read_bytes()==(OUT/name).read_bytes(),f'Published file out of sync: {name}'
assert (ROOT/'index.html').is_file() and (ROOT/'.nojekyll').is_file()
assert (ROOT/'CNAME').read_text().strip()==urlsplit(BASE).netloc
print('PASS: main/root contains the complete generated site and matches the configured custom domain.')
