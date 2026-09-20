import re

with open('index.html', 'rb') as f:
    raw = f.read()

print('Has BOM:', raw[:3] == b'\xef\xbb\xbf')
text = raw.decode('utf-8')

if 'Yeni Makale' in text:
    matches = re.findall(r'<h2 class="card-title">\s*<a[^>]*>([^<]*)</a>', text)
    print(f'Cards with "Yeni Makale": {text.count("Yeni Makale")}')
    for m in matches:
        print(f'  - {m[:80]}')
else:
    print('No "Yeni Makale" found - all good!')
    matches = re.findall(r'<h2 class="card-title">\s*<a[^>]*>([^<]*)</a>', text)
    print(f'Total cards: {len(matches)}')
    for m in matches:
        print(f'  - {m[:80]}')
