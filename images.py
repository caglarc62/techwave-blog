"""
images.py — Unsplash API ile makale görselleri çeker.
Ücretsiz Unsplash demo erişimi ile çalışır.
"""

import os
import re
import hashlib
import logging
import requests
import time

log = logging.getLogger("content_bot.images")

# Unsplash demo access key (rate limit: 50 istek/saat)
# Kendi key'ini https://unsplash.com/developers adresinden alabilirsin
UNSPLASH_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY", "")

# Görsel boyutları
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630  # OG image standardı

# Yedek görseller (Unsplash çalışmazsa)
FALLBACK_IMAGES = {
    "Yapay Zeka": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=1200&h=630&fit=crop",
    "Yazılım": "https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1200&h=630&fit=crop",
    "Python": "https://images.unsplash.com/photo-1526379095098-d400fd0bf935?w=1200&h=630&fit=crop",
    "AI Araçları": "https://images.unsplash.com/photo-1684163761883-8cba5e0004e0?w=1200&h=630&fit=crop",
    "Siber Güvenlik": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1200&h=630&fit=crop",
    "Mobil": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=1200&h=630&fit=crop",
    "Oyun": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1200&h=630&fit=crop",
    "Bulut Bilişim": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=1200&h=630&fit=crop",
    "Veri Bilimi": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=630&fit=crop",
    "Blockchain": "https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=1200&h=630&fit=crop",
}

# İngilizce arama sorguları (kategori bazlı)
CATEGORY_SEARCH_TERMS = {
    "Yapay Zeka": "artificial intelligence robot technology",
    "Yazılım": "software development coding programming",
    "Python": "python programming code screen",
    "AI Araçları": "ai chatbot digital assistant technology",
    "Siber Güvenlik": "cybersecurity digital lock protection",
    "Mobil": "smartphone mobile app technology",
    "Oyun": "gaming setup esports video game",
    "Bulut Bilişim": "cloud computing server data center",
    "Veri Bilimi": "data analytics charts dashboard",
    "Blockchain": "blockchain cryptocurrency network",
}


def search_unsplash(query, count=1):
    """Unsplash API ile görsel arar."""
    if not UNSPLASH_ACCESS_KEY:
        log.info("Unsplash API key yok, fallback görseller kullanılıyor.")
        return []

    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "per_page": count,
        "orientation": "landscape",
        "client_id": UNSPLASH_ACCESS_KEY,
    }

    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code == 200:
            data = resp.json()
            results = data.get("results", [])
            return [
                {
                    "url": r["urls"]["regular"],
                    "thumb": r["urls"]["small"],
                    "author": r["user"]["name"],
                    "author_url": r["user"]["links"]["html"],
                    "description": r.get("description", ""),
                }
                for r in results
            ]
        elif resp.status_code == 403:
            log.warning("Unsplash rate limit aşıldı (403).")
            return []
        else:
            log.warning("Unsplash API hatası: %d", resp.status_code)
            return []
    except Exception as e:
        log.warning("Unsplash isteği başarısız: %s", e)
        return []


def get_article_image(category, title=""):
    """Makale için görsel URL'i döndürür."""
    # 1. Unsplash'ta ara
    search_query = CATEGORY_SEARCH_TERMS.get(category, f"{category} technology")
    if title:
        # Başlıktan anahtar kelimeler çıkar
        title_words = re.sub(r'[^\w\s]', '', title.lower()).split()[:3]
        search_query = " ".join(title_words) + " " + " ".join(search_query.split()[-2:])

    results = search_unsplash(search_query)
    if results:
        image_url = results[0]["url"]
        author = results[0]["author"]
        log.info("Unsplash görseli bulundu: %s (by %s)", image_url[:60], author)
        return {
            "url": image_url,
            "thumb": results[0]["thumb"],
            "author": author,
            "author_url": results[0]["author_url"],
            "credit": f"Fotoğraf: {author} / Unsplash",
            "source": "unsplash",
        }

    # 2. Fallback görsel kullan
    fallback_url = FALLBACK_IMAGES.get(
        category,
        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1200&h=630&fit=crop"
    )
    log.info("Fallback görsel kullanılıyor: %s", category)
    return {
        "url": fallback_url,
        "thumb": fallback_url,
        "author": "Unsplash",
        "author_url": "https://unsplash.com",
        "credit": "Fotoğraf: Unsplash",
        "source": "fallback",
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    from dotenv import load_dotenv
    load_dotenv()

    for cat in ["Yapay Zeka", "Python", "Siber Güvenlik"]:
        img = get_article_image(cat, f"{cat} rehberi")
        print(f"\n{cat}:")
        print(f"  URL: {img['url'][:80]}")
        print(f"  Credit: {img['credit']}")
