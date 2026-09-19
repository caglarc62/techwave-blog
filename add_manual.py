import sys
sys.path.insert(0, '.')
from update_index import create_card_html

article = {
    "title": "2026'da Akıllı Telefon Alırken Yapılan 5 Kritik Hata ve Doğru Tercih Rehberi",
    "slug": "2026-telefon-alirken-5-kritik-hata",
    "excerpt": "Teknoloji dünyası her geçen gün daha hızlı gelişiyor. Doğru cihazı seçmek, sadece en pahalı modeli satın almaktan geçmiyor.",
    "category": "Mobil",
    "emoji": "📱",
    "gradient": "linear-gradient(135deg, #667eea, #764ba2)",
    "image_url": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=600",
    "date": "19 Eylül 2026",
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
