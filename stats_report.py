from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json, re

env = {}
for line in open('.env', encoding='utf-8'):
    if '=' in line and not line.startswith('#'):
        k, v = line.strip().split('=', 1)
        env[k] = v
token = env['METRIKA_OAUTH_TOKEN']


def query(metrics, dimensions, date1, date2, filters=None, limit=100, sort=None):
    params = {
        'ids': '112858721',
        'metrics': metrics,
        'dimensions': dimensions,
        'date1': date1,
        'date2': date2,
        'limit': str(limit),
    }
    if filters:
        params['filters'] = filters
    if sort:
        params['sort'] = sort
    url = 'https://api-metrika.yandex.net/stat/v1/data?' + urlencode(params)
    req = Request(url, headers={'Authorization': 'OAuth ' + token})
    data = json.loads(urlopen(req, timeout=30).read().decode('utf-8'))
    rows = []
    for row in data.get('data', []):
        dims = [d.get('name', '') for d in row.get('dimensions', [])]
        mets = row.get('metrics', [])
        vals = []
        for m in mets:
            if isinstance(m, dict):
                vals.append(m.get('values', [''])[0])
            else:
                vals.append(m)
        rows.append((dims, vals))
    return rows


print('=== SON 30 GUN: SAYFA GORUNTULEMELERI (top 25) ===')
rows = query('ym:s:pageviews,ym:s:users', 'ym:s:startURL',
             '2026-08-30', '2026-09-28',
             sort='-ym:s:pageviews', limit=25)
total_pv = sum(float(r[1][0]) for r in rows)
for dims, vals in rows:
    url = dims[0]
    path = url.replace('https://techwaveblog.site', '') or '/'
    print('%6s goruntuleme | %4s ziyaretci | %s' % (int(float(vals[0])), int(float(vals[1])), path))

print()
print('=== DUN (27 Eylul) ===')
rows = query('ym:s:pageviews,ym:s:users', 'ym:s:startURL',
             '2026-09-27', '2026-09-27', sort='-ym:s:pageviews', limit=10)
for dims, vals in rows:
    path = dims[0].replace('https://techwaveblog.site', '') or '/'
    print('%6s | %4s | %s' % (int(float(vals[0])), int(float(vals[1])), path))

print()
print('=== BUGUN (28 Eylul) ===')
rows = query('ym:s:pageviews,ym:s:users', 'ym:s:startURL',
             '2026-09-28', '2026-09-28', sort='-ym:s:pageviews', limit=10)
for dims, vals in rows:
    path = dims[0].replace('https://techwaveblog.site', '') or '/'
    print('%6s | %4s | %s' % (int(float(vals[0])), int(float(vals[1])), path))
