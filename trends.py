"""
trends.py — Güncel teknoloji trendlerini tarar ve konu önerir.
Google News RSS feed'lerini ve web aramasını kullanır.
"""

import re
import os
import random
import logging
from datetime import datetime

import requests

log = logging.getLogger("content_bot.trends")


def get_used_topics(articles_dir):
    """Önceki makalelerin başlıklarını okur — tekrarları önlemek için."""
    used = set()
    if not os.path.exists(articles_dir):
        return used
    for fname in os.listdir(articles_dir):
        if fname.endswith(".html"):
            # Dosya adından başlığı çıkar (tire ve uzantıyı temizle)
            slug = fname.replace(".html", "")
            used.add(slug.lower())
    return used


def is_topic_used(title, used_topics):
    """Konu başlığının daha önce kullanılıp kullanılmadığını kontrol eder."""
    slug = re.sub(r'[^a-z0-9\s-]', '', title.lower()).replace(" ", "-").strip("-")[:50]
    return slug in used_topics

# Engellenmiş kelimeler — makale konusu olarak uygun olmayanlar
STOP_WORDS = {
    "dolar", "borsa", "piyasa", "kripto para", "bitcoin fiyatı",
    "altcoin", "yatırım", "kazanç", "fırsat", "indirim", "kampanya",
    "ücretsiz", "bedava", "hediye", "çekiliş", "maç", "spor",
    "magazin", "gélin", "düğün", "İngiltere", "Amerika seçimi",
}


def fetch_rss_feed(url, timeout=15):
    """RSS feed'inden haber başlıklarını çeker."""
    try:
        resp = requests.get(url, timeout=timeout, headers={
            "User-Agent": "TechWave ContentBot/1.0"
        })
        if resp.status_code != 200:
            log.warning("RSS feed alınamadı (%s): %d", url, resp.status_code)
            return []

        items = re.findall(r"<title>(.*?)</title>", resp.text)
        # İlk başlık genellikle feed adı, onu atla
        return [item for item in items[1:] if len(item) > 15]
    except Exception as e:
        log.warning("RSS hatası (%s): %s", url, e)
        return []


def search_web_trends(query="technology AI trends 2026", num_results=8):
    """Basit web araması ile trend konular çeker (API gerekmez)."""
    try:
        url = "https://duckduckgo.com/html/"
        params = {"q": query}
        resp = requests.get(url, params=params, timeout=15, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        })
        if resp.status_code != 200:
            return []

        titles = re.findall(r'class="result__a"[^>]*>(.*?)</a>', resp.text)
        return [re.sub(r'<[^>]+>', '', t) for t in titles[:num_results]]
    except Exception as e:
        log.warning("Web arama hatası: %s", e)
        return []


def extract_topics_from_headlines(headlines):
    """Haber başlıklarından potansiyel makale konuları çıkarır."""
    topic_keywords = {
        "Yapay Zeka": [
            "yapay zeka", "ai", "artificial intelligence", "chatgpt",
            "claude", "gemini", "llm", "deep learning", "machine learning",
            "neural", "gpt", "openai", "anthropic", "deepseek"
        ],
        "Yazılım": [
            "yazılım", "software", "programming", "kod", "code",
            "developer", "github", "open source", "api", "framework",
            "javascript", "typescript", "rust", "golang"
        ],
        "Python": [
            "python", "django", "flask", "pandas", "numpy",
            "jupyter", "pip", "conda"
        ],
        "AI Araçları": [
            "ai tool", "chatbot", "copilot", "assistant",
            "ai agent", "automation", "midjourney", "dall-e", "suno"
        ],
        "Siber Güvenlik": [
            "güvenlik", "security", "hack", "cyber", "vulnerability",
            "ransomware", "phishing", "data breach", "privacy"
        ],
        "Mobil": [
            "mobil", "mobile", "android", "ios", "iphone",
            "samsung", "uygulama", "app", "tablet"
        ],
        "Oyun": [
            "oyun", "game", "gaming", "playstation", "xbox",
            "nintendo", "steam", "espor"
        ],
        "Bulut Bilişim": [
            "bulut", "cloud", "aws", "azure", "google cloud",
            "serverless", "kubernetes", "docker"
        ],
        "Veri Bilimi": [
            "veri", "data", "analytics", "big data", "database",
            "sql", "nosql", "visualization"
        ],
        "Blockchain": [
            "blockchain", "web3", "defi", "nft", "ethereum",
            "solana", "smart contract"
        ],
    }

    found_topics = {}

    for headline in headlines:
        headline_lower = headline.lower()

        # Engellenmiş kelimeler kontrolü
        if any(sw in headline_lower for sw in STOP_WORDS):
            continue

        for category, keywords in topic_keywords.items():
            for kw in keywords:
                if kw in headline_lower:
                    if category not in found_topics:
                        found_topics[category] = []
                    found_topics[category].append(headline)
                    break

    return found_topics


def generate_topic_from_trends(trend_sources, web_queries=None):
    """Trend kaynaklarından rastgele bir konu üretir — tekrarları atlar."""
    import json
    
    # Daha önce kullanılmış konuları yükle
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
        articles_dir = os.path.join(os.path.dirname(__file__), config.get("articles_dir", "articles"))
    except Exception:
        articles_dir = os.path.join(os.path.dirname(__file__), "articles")
    
    used_topics = get_used_topics(articles_dir)
    log.info("Daha önce %d makale yayınlanmış.", len(used_topics))
    all_headlines = []

    # RSS feed'lerinden çek
    for url in trend_sources:
        headlines = fetch_rss_feed(url)
        all_headlines.extend(headlines)
        log.info("RSS'den %d başlık çekildi: %s", len(headlines), url)

    # Web araması
    if web_queries is None:
        web_queries = [
            "yapay zeka son gelişmeler 2026",
            "yeni teknoloji trendleri 2026",
            "yazılım dünyası güncel haberler",
        ]

    for query in web_queries:
        results = search_web_trends(query)
        all_headlines.extend(results)
        log.info("Web'den %d sonuç çekildi: %s", len(results), query)

    if not all_headlines:
        log.warning("Hiç trend başlık bulunamadı, rastgele konu üretiliyor.")
        return generate_random_topic()

    # Konuları çıkar
    topics = extract_topics_from_headlines(all_headlines)

    if not topics:
        log.warning("Başlıklardan konu çıkarılamadı, rastgele konu üretiliyor.")
        return generate_random_topic()

    # Kullanılmamış konuları filtrele
    filtered_topics = {}
    for cat, headlines in topics.items():
        valid = [h for h in headlines if not is_topic_used(h, used_topics)]
        if valid:
            filtered_topics[cat] = valid

    if not filtered_topics:
        log.warning("Tüm trend konuları daha önce kullanılmış, rastgele konu üretiliyor.")
        return generate_random_topic()

    # Rastgele bir kategori ve konu seç
    category = random.choice(list(filtered_topics.keys()))
    headline = random.choice(filtered_topics[category])

    # Başlığı temizle
    clean_title = re.sub(r'[^\w\sğüşıöçĞÜŞİÖÇ-]', '', headline)
    clean_title = ' '.join(clean_title.split()[:12])

    return {
        "category": category,
        "title": clean_title,
        "source_headline": headline,
    }


def generate_random_topic():
    """Rastgele bir konu üretir (trend bulunamadığında)."""
    fallback_topics = [
        {"category": "Yapay Zeka", "title": "Yeni Nesil Dil Modelleri ve Geleceği"},
        {"category": "Yazılım", "title": "2026'da Öğrenilmesi Gereken Programlama Dilleri"},
        {"category": "Python", "title": "Python ile Veri Görselleştirme Rehberi"},
        {"category": "AI Araçları", "title": "İş Hayatında Yapay Zeka Kullanım Alanları"},
        {"category": "Siber Güvenlik", "title": "Kişisel Verilerinizi Nasıl Korursunuz"},
        {"category": "Mobil", "title": "Mobil Uygulama Geliştirme Trendleri 2026"},
        {"category": "Oyun", "title": "Oyun Endüstrisinde Yapay Zeka Kullanımı"},
        {"category": "Bulut Bilişim", "title": "Bulut Bilişime Geçiş Rehberi"},
        {"category": "Veri Bilimi", "title": "Veri Bilimine Giriş: Temel Kavramlar"},
        {"category": "Blockchain", "title": "Blockchain Teknolojisinin Günlük Hayattaki Yeri"},
    ]

    topic = random.choice(fallback_topics)
    log.info("Rastgele konu seçildi: %s - %s", topic["category"], topic["title"])
    return topic


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    from dotenv import load_dotenv
    load_dotenv()

    with open("config.json", "r", encoding="utf-8") as f:
        import json
        config = json.load(f)

    topic = generate_topic_from_trends(config["trend_sources"])
    print(f"\nSeçilen Konu:")
    print(f"  Kategori: {topic['category']}")
    print(f"  Başlık:   {topic['title']}")
    print(f"  Kaynak:   {topic.get('source_headline', 'Yok')}")
