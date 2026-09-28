import os, re, json, html as htmlmod

ART_DIR = 'articles'
OUT = 'search-index.json'

def strip_tags(s):
    s = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', s, flags=re.DOTALL | re.IGNORECASE)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = htmlmod.unescape(s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def grab(content, pattern, default=''):
    m = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else default

items = []
for fname in sorted(os.listdir(ART_DIR)):
    if not fname.endswith('.html'):
        continue
    path = os.path.join(ART_DIR, fname)
    with open(path, encoding='utf-8') as f:
        c = f.read()

    slug = fname[:-5]
    title = grab(c, r'<h1[^>]*>(.*?)</h1>')
    title = strip_tags(title)
    category = grab(c, r'data-category="([^"]+)"', 'Genel')
    excerpt = grab(c, r'<meta name="description" content="([^"]*)"')
    if not excerpt:
        excerpt = grab(c, r'<p class="card-excerpt">(.*?)</p>')
    excerpt = htmlmod.unescape(excerpt)
    date = grab(c, r'📅\s*([^<]+)</span>', '')

    # headings (h2/h3) for search boost
    headings = [strip_tags(h) for h in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', c, re.DOTALL)]
    headings = [h for h in headings if h]

    # body text truncated
    body = grab(c, r'<div class="article-content"[^>]*>(.*)', '')
    body = strip_tags(body)[:1200]

    items.append({
        't': title,
        's': slug,
        'c': category,
        'e': excerpt[:200],
        'd': date,
        'h': ' | '.join(headings[:8]),
        'x': body,
    })

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, separators=(',', ':'))

size = os.path.getsize(OUT)
print('%d makale, %d KB' % (len(items), size // 1024))
