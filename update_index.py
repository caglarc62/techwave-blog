"""
update_index.py — Ana sayfaya yeni makale kartı ekler (görselli).
"""

import os
import re
import logging
from datetime import datetime

log = logging.getLogger("content_bot.index updater")


def create_card_html(article):
    """Yeni makale kartı HTML'i oluşturur (görselli)."""
    emoji = article.get("emoji", "📝")
    gradient = article.get("gradient", "linear-gradient(135deg, #667eea, #764ba2)")
    category = article.get("category", "Teknoloji")
    title = article.get("title", "Yeni Makale")
    slug = article.get("slug", "yeni-makale")
    excerpt = article.get("excerpt", "")
    months_tr = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan",
        5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
        9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık",
    }
    now = datetime.now()
    date = article.get("date", f"{now.day} {months_tr[now.month]} {now.year}")
    read_time = article.get("read_time", "5 dk okuma")

    # Görsel varsa kullan, yoksa gradient + emoji
    image_url = article.get("image_url", "")
    if image_url:
        img_html = f'<img src="{image_url}" alt="{title}" loading="lazy">'
    else:
        img_html = f'<div style="display:flex; align-items:center; justify-content:center; color:#fff; font-size:2rem; height:100%; background:{gradient};">{emoji}</div>'

    return f'''        <!-- YENİ MAKALE — Otomatik eklendi -->
        <article class="card">
          <div class="card-img">{img_html}</div>
          <div class="card-body">
            <span class="card-tag">{category}</span>
            <h2 class="card-title">
              <a href="articles/{slug}.html">{title}</a>
            </h2>
            <p class="card-excerpt">{excerpt}</p>
            <div class="card-meta">
              <span>📅 {date}</span>
              <span>⏱️ {read_time}</span>
            </div>
          </div>
        </article>'''


def update_index_html(article, site_dir):
    """index.html'e yeni makale kartı en üste ekler."""
    index_path = os.path.join(site_dir, "index.html")

    if not os.path.exists(index_path):
        log.error("index.html bulunamadı: %s", index_path)
        return False

    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    card_html = create_card_html(article)

    # Her zaman card-grid'in hemen sonrasına ekle (en üste)
    grid_marker = '<div class="card-grid">'
    if grid_marker in content:
        content = content.replace(
            grid_marker,
            grid_marker + "\n\n" + card_html + "\n",
            1
        )
    else:
        log.error("index.html'de card-grid bulunamadı.")
        return False

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)

    log.info("index.html güncellendi: %s makale en üste eklendi.", article.get("title"))
    return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    test_article = {
        "emoji": "🤖",
        "gradient": "linear-gradient(135deg, #667eea, #764ba2)",
        "category": "Yapay Zeka",
        "title": "Test Makalesi",
        "slug": "test-makalesi",
        "excerpt": "Bu bir test makalesidir.",
        "date": "7 Eylül 2026",
        "read_time": "5 dk okuma",
        "image_url": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&h=360&fit=crop",
    }
    card = create_card_html(test_article)
    print(card)
