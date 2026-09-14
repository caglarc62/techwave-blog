import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

grid_start = content.find('<div class="card-grid">')
if grid_start < 0:
    print('card-grid bulunamadi')
    exit()

articles = re.findall(r'<article class="card">.*?</article>', content[grid_start:], re.DOTALL)

seen = set()
duplicates = []
for i, art in enumerate(articles):
    title_match = re.search(r'<a href="[^"]+">(.*?)</a>', art)
    if title_match:
        title = title_match.group(1).strip()
        if title in seen:
            duplicates.append((i, title, art))
        seen.add(title)

print(f'Toplam kart: {len(articles)}')
print(f'Tekrar sayisi: {len(duplicates)}')
for idx, title, _ in duplicates:
    print(f'  Tekrar {idx}: {title[:60]}')

# Tekrarlanan kartları sil
if duplicates:
    new_content = content
    for _, title, art in duplicates:
        # Kartı HTML'den çıkar
        clean_art = art.strip()
        new_content = new_content.replace(clean_art + '\n\n', '')
        new_content = new_content.replace(clean_art, '')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'\n{len(duplicates)} tekrar silindi!')
else:
    print('\nTekrar yok.')
