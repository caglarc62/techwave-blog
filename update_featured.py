import os, re, json, sys
from datetime import datetime, timedelta
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError

BASE = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(BASE, 'index.html')
ENV = os.path.join(BASE, '.env')
COUNTER_ID = '112858721'


def load_env():
    env = {}
    if os.path.exists(ENV):
        for line in open(ENV, encoding='utf-8'):
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                k, v = line.split('=', 1)
                env[k.strip()] = v.strip()
    return env


def fetch_top_articles(token, days=30):
    date1 = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    date2 = datetime.now().strftime('%Y-%m-%d')
    params = {
        'ids': COUNTER_ID,
        'metrics': 'ym:s:pageviews',
        'dimensions': 'ym:s:startURL',
        'filters': "ym:s:startURL=~'/articles/'",
        'date1': date1,
        'date2': date2,
        'limit': '500',
        'sort': '-ym:s:pageviews',
    }
    url = 'https://api-metrika.yandex.net/stat/v1/data?' + urlencode(params)
    req = Request(url, headers={'Authorization': 'OAuth ' + token})
    try:
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
    except HTTPError as e:
        print('Metrica API HTTP hatasi: %s %s' % (e.code, e.read().decode('utf-8', 'ignore')[:300]))
        sys.exit(1)
    except URLError as e:
        print('Baglanti hatasi: %s' % e)
        sys.exit(1)

    results = []
    for row in data.get('data', []):
        dims = row.get('dimensions', [])
        mets = row.get('metrics', [])
        path = dims[0].get('name', '') if dims else ''
        views = 0
        try:
            m0 = mets[0]
            if isinstance(m0, dict):
                m0 = m0.get('values', [0])[0]
            views = int(float(m0))
        except (ValueError, IndexError, TypeError):
            pass
        m = re.search(r'/articles/([^/?#]+?)(?:\.html)?(?:[?#]|$)', path)
        if m:
            results.append((m.group(1), views))
    results.sort(key=lambda x: -x[1])
    return results


def write_popular(top, limit=5):
    titles = {}
    idx_path = os.path.join(BASE, 'search-index.json')
    if os.path.exists(idx_path):
        for it in json.load(open(idx_path, encoding='utf-8')):
            titles[it['s']] = it['t']
    items = [{'s': s, 'v': v, 't': titles[s]} for s, v in top if s in titles][:limit]
    if not items:
        return
    out = os.path.join(BASE, 'popular.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, separators=(',', ':'))
    print('popular.json guncellendi (%d makale)' % len(items))


def parse_featured(content):
    m = re.search(r'      <div class="featured-post">.*?\n      </div>\n', content, re.DOTALL)
    if not m:
        raise SystemExit('featured-post blogu bulunamadi')
    return m


def parse_card(content, slug):
    href = 'href="articles/%s.html"' % slug
    block = None
    for m in re.finditer(r'        <article class="card"[^>]*>.*?</article>\n', content, re.DOTALL):
        if href in m.group(0):
            block = m.group(0)
            break
    if not block:
        return None, None

    def grab(pattern, default=''):
        g = re.search(pattern, block, re.DOTALL)
        return g.group(1).strip() if g else default

    cat = grab(r'data-category="([^"]*)"')
    info = {
        'slug': slug,
        'cat': cat,
        'category': cat,
        'img': grab(r'<img src="([^"]+)"'),
        'alt': grab(r'<img src="[^"]+" alt="([^"]*)"'),
        'title': grab(r'<a href="articles/[^"]+">([^<]+)</a>'),
        'excerpt': grab(r'<p class="card-excerpt">(.*?)</p>'),
        'date': grab(r'📅\s*([^<]+)</span>'),
        'read': grab(r'⏱️\s*([^<]+)</span>'),
    }
    if not info['title'] or not info['img']:
        return None, None
    return block, info


def parse_old_featured(content):
    block = parse_featured(content).group(0)
    img = re.search(r'<img src="([^"]+)" alt="([^"]*)"', block)
    title = re.search(r'<a href="articles/([^"]+)\.html">([^<]+)</a>', block)
    cat = re.search(r'data-category="([^"]+)"', block)
    excerpt = re.search(r'<p class="card-excerpt">(.*?)</p>', block, re.DOTALL)
    date = re.search(r'📅\s*([^<]+)</span>', block)
    read = re.search(r'⏱️\s*([^<]+)</span>', block)
    return {
        'slug': title.group(1) if title else '',
        'img': img.group(1) if img else '',
        'alt': img.group(2) if img else '',
        'title': title.group(2) if title else '',
        'category': cat.group(1) if cat else '',
        'excerpt': excerpt.group(1).strip() if excerpt else '',
        'date': date.group(1).strip() if date else '',
        'read': read.group(1).strip() if read else '',
    }


def make_featured(info):
    return (
        '      <div class="featured-post">\n'
        '        <article class="featured-card">\n'
        '          <div class="card-img">\n'
        '            <img src="{img}" alt="{alt}" loading="eager">\n'
        '          </div>\n'
        '          <div class="card-body">\n'
        '            <span class="featured-badge">⭐ Öne Çıkan</span>\n'
        '            <span class="card-tag" data-category="{cat}">{cat}</span>\n'
        '            <h2 class="card-title">\n'
        '              <a href="articles/{slug}.html">{title}</a>\n'
        '            </h2>\n'
        '            <p class="card-excerpt">{excerpt}</p>\n'
        '            <div class="card-meta">\n'
        '              <span>📅 {date}</span>\n'
        '              <span>⏱️ {read}</span>\n'
        '            </div>\n'
        '          </div>\n'
        '        </article>\n'
        '      </div>\n'
    ).format(
        img=info['img'], alt=info['alt'], cat=info['category'],
        slug=info['slug'], title=info['title'], excerpt=info['excerpt'],
        date=info['date'], read=info['read'],
    )


def make_card(info):
    return (
        '        <article class="card" data-category="{cat}">\n'
        '          <div class="card-img"><img src="{img}" alt="{alt}" loading="lazy"></div>\n'
        '          <div class="card-body">\n'
        '            <span class="card-tag" data-category="{cat}">{cat}</span>\n'
        '            <h2 class="card-title">\n'
        '              <a href="articles/{slug}.html">{title}</a>\n'
        '            </h2>\n'
        '            <p class="card-excerpt">{excerpt}</p>\n'
        '            <div class="card-meta">\n'
        '              <span>📅 {date}</span>\n'
        '              <span>⏱️ {read}</span>\n'
        '            </div>\n'
        '          </div>\n'
        '        </article>\n'
    ).format(**info)


def main():
    env = load_env()
    token = env.get('METRIKA_OAUTH_TOKEN', '')
    if not token:
        print('METRIKA_OAUTH_TOKEN .env dosyasinda yok. Once token alin.')
        sys.exit(1)

    top = fetch_top_articles(token)
    if not top:
        print('Son 30 gunde makale trafigi bulunamadi.')
        sys.exit(0)

    print('En cok okunan makaleler (son 30 gun):')
    for slug, views in top[:5]:
        print('  %s -> %d gosterim' % (slug, views))

    write_popular(top)

    content = open(INDEX, encoding='utf-8').read()
    old_feat = parse_old_featured(content)

    winner = top[0][0]
    if winner == old_feat['slug']:
        print('Zaten en cok okunan makale one cikan. Degisiklik yok.')
        return

    card_block, info = parse_card(content, winner)
    if not card_block:
        print('Kart bulunamadi: %s' % winner)
        sys.exit(1)

    # Yeni one cikani kur
    fm = parse_featured(content)
    content = content[:fm.start()] + make_featured(info) + content[fm.end():]
    # Kazanan karti grid'den cikar
    content = content.replace(card_block, '', 1)
    # Eski one cikani normal karta cevirip kazananin oldugu yere koy
    old_card = make_card({**old_feat, 'cat': old_feat['category'], 'category': old_feat['category']})
    grid_start = content.index('<div class="card-grid">')
    insert_at = content.index('\n', grid_start) + 1
    content = content[:insert_at] + '\n' + old_card + content[insert_at:]

    open(INDEX, 'w', encoding='utf-8').write(content)
    print('OK: %s artik one cikan.' % winner)


if __name__ == '__main__':
    main()
