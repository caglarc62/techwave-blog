import sys
sys.path.insert(0, '.')
from update_index import create_card_html

article = {
    "title": "2026 Piyasa Dinamikleri: Algoritmik Ticaret, Küresel Makro Veriler ve Kripto Piyasalarının Yönü",
    "slug": "2026-piyasa-dinamikleri-algoritmik-ticaret-kripto",
    "excerpt": "Küresel faiz politikaları, BIST 100, Bitcoin ETF akışları ve algoritmik ticaret stratejileri: 2026 finans dünyasının tamamı.",
    "category": "Finans",
    "emoji": "📈",
    "gradient": "linear-gradient(135deg, #11998e, #38ef7d)",
    "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=600",
    "date": "20 Eylül 2026",
    "read_time": "6 dk okuma"
}

card = create_card_html(article)

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

grid_marker = '<div class="card-grid">'
idx = content.find(grid_marker)
if idx >= 0:
    insert_pos = idx + len(grid_marker)
    new_content = content[:insert_pos] + "\n\n" + card + "\n\n" + content[insert_pos:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Index guncellendi!")
else:
    print("card-grid bulunamadi!")
