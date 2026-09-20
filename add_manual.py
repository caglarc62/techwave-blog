import sys
sys.path.insert(0, '.')
from update_index import create_card_html

article = {
    "title": "2026'da İşletim Sistemi ve Kodlama Dünyasını Şekillendiren Teknoloji Trendleri",
    "slug": "2026-isletim-sistemi-ve-kodlama-teknoloji-trendleri",
    "excerpt": "Teknoloji dünyasında yeniliklerin hızı kesilmiyor. Yerleşik yapay zeka, on-device AI, cross-platform diller ve daha fazlası.",
    "category": "Yazılım",
    "emoji": "💻",
    "gradient": "linear-gradient(135deg, #667eea, #764ba2)",
    "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600",
    "date": "20 Eylül 2026",
    "read_time": "5 dk okuma"
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
