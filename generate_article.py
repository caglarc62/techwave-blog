"""
generate_article.py — Google Gemini API ile SEO uyumlu makale üretir.
"""

import os
import json
import logging
import re
from datetime import datetime

import google.generativeai as genai
import images

log = logging.getLogger("content_bot.generator")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def configure_client():
    """Gemini API istemcisini yapılandırır."""
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        raise ValueError("GEMINI_API_KEY ortam değişkeni ayarlanmamış!")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-3.6-flash")


def build_system_prompt():
    """Sistem promptunu döndürür."""
    return """Sen TechWave için uzman bir teknoloji yazarısın.
Görevin, verilen konuda bilgilendirici, akıcı ve SEO uyumlu Türkçe makaleler yazmak.

YAZI KURALLARI:
- 800-1200 kelime arası yaz
- H1 başlığını makale başlığı olarak kullan (sadece metin, HTML değil)
- H2 ve H3 alt başlıklar kullan
- Kısa paragraflar yaz (3-5 cümle)
- Pratik örnekler ve ipuçları ekle
- Teknik terimleri açıkla
- Samimi ama profesyonel bir dil kullan
- Lists (ul/ol) ve blockquote kullan
- Kod örnekleri varsa ``` ile ver
- SEO anahtar kelimelerini doğal kullan

ÇIKTI FORMATI:
Makale içeriğini şu JSON formatında döndür:
{
    "title": "Makale Başlığı (H1)",
    "slug": "makale-basligi-url",
    "excerpt": "150 karakterlik özet",
    "content": "HTML içeriği (body bölümü, script ve style hariç)",
    "meta_description": "160 karakterlik SEO açıklaması",
    "tags": ["etiket1", "etiket2", "etiket3"]
}

ÖNEMLİ: Sadece JSON döndür, başka hiçbir metin ekleme. JSON bloğunu ```json ... ``` içine al."""


def build_user_prompt(topic_info, config):
    """Kullanıcı promptunu oluşturur."""
    category = topic_info["category"]
    title = topic_info["title"]
    min_words = config.get("article_min_words", 1500)
    max_words = config.get("article_max_words", 2500)

    return f"""Şu konuda TechWave için detaylı bir makale yaz:

Kategori: {category}
Konu: {title}

Gereksinimler:
- En az {min_words} kelime olsun, kapsamlı ve detaylı yaz
- SEO uyumlu (meta description, etiketler dahil)
- Pratik örnekler, istatistikler ve güncel bilgiler içer
- H2 ve H3 alt başlıklar kullan (en az 3-4 alt başlık)
- Kod örneği varsa ekle
- Giriş gelişme sonuç bölümleri olsun
- Benzer konulardaki farklı bakış açılarını da ekle
- OKUYUCUYA DEĞER KAT: Sadece bilgi verme, ipuçları, tavsiyeler ve somut örnekler ekle
- Türkçe, akıcı ve bilgilendirici dil
- Makale sonunda "Bu makale TechWave tarafından hazırlanmıştır." ekle

JSON formatında döndür."""


def generate_article(topic_info, config):
    """Gemini API ile makale üretir — hata olursa tekrar dener."""
    model = configure_client()

    system_prompt = build_system_prompt()
    user_prompt = build_user_prompt(topic_info, config)

    full_prompt = f"{system_prompt}\n\n{user_prompt}"

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        log.info("Gemini API'ye istek gönderiliyor... (deneme %d/%d)", attempt, max_retries)

        try:
            response = model.generate_content(full_prompt)
            raw_text = response.text
            log.info("Gemini yanıtı alındı. Uzunluk: %d karakter", len(raw_text))

            # JSON'u parse et
            article_data = parse_article_response(raw_text)

            if article_data is None:
                log.error("Deneme %d: JSON parse başarısız.", attempt)
                if attempt < max_retries:
                    log.info("Tekrar deneniyor...")
                    continue
                else:
                    # Son deneme: ham yanıtı dosyaya kaydet (debug için)
                    debug_path = os.path.join(SCRIPT_DIR, "last_failed_response.txt")
                    with open(debug_path, "w", encoding="utf-8") as f:
                        f.write(raw_text)
                    log.error("Ham yanıt kaydedildi: %s", debug_path)
                    return None

        # Başarılı — devam et
            break

        except Exception as e:
            log.error("Gemini API hatası (deneme %d): %s", attempt, e)
            if attempt < max_retries:
                # 429 hatası ise bekle
                if "429" in str(e) or "quota" in str(e).lower():
                    wait_time = 65
                    log.info("Kota aşıldı, %d saniye bekleniyor...", wait_time)
                    import time
                    time.sleep(wait_time)
                else:
                    log.info("Tekrar deneniyor...")
                continue
            return None

    # Kategori ve emoji bilgilerini ekle
    article_data["category"] = topic_info["category"]
    article_data["emoji"] = config.get("emoji_map", {}).get(topic_info["category"], "📝")
    article_data["gradient"] = config.get("gradient_map", {}).get(
        topic_info["category"], "linear-gradient(135deg, #667eea, #764ba2)"
    )

    # Görsel çek
    log.info("Görsel aranıyor...")
    try:
        image_info = images.get_article_image(
            topic_info["category"],
            article_data.get("title", "")
        )
        article_data["image_url"] = image_info["url"]
        article_data["image_thumb"] = image_info["thumb"]
        article_data["image_credit"] = image_info["credit"]
        log.info("Görsel eklendi: %s", image_info["source"])
    except Exception as e:
        log.warning("Görsel alınamadı, gradient kullanılıyor: %s", e)
        article_data["image_url"] = ""
        article_data["image_credit"] = ""

    now = datetime.now()
    months_tr = {
        1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan",
        5: "Mayıs", 6: "Haziran", 7: "Temmuz", 8: "Ağustos",
        9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık",
    }
    article_data["date"] = f"{now.day} {months_tr[now.month]} {now.year}"
    article_data["date_iso"] = now.strftime("%Y-%m-%d")
    article_data["author"] = config.get("author", "TechWave")
    article_data["read_time"] = estimate_read_time(article_data.get("content", ""))

    return article_data


def parse_article_response(raw_text):
    """Gemini yanıtından JSON'u çıkarır — çoklu deneme stratejisi."""
    # Adım 0: Markdown code block'larını temizle (```json ... ```)
    json_match = re.search(r'```json\s*(.*?)\s*```', raw_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
    else:
        json_str = raw_text.strip()
        if not json_str.startswith('{'):
            start = json_str.find('{')
            end = json_str.rfind('}') + 1
            if start >= 0 and end > start:
                json_str = json_str[start:end]

    # Adım 0.5: HTML code block'larındaki " karakterlerini escape et
    # <pre><code class="language-python"> → class=\\"language-python\\"
    def escape_html_quotes(m):
        return m.group(0).replace('"', '\\"')
    json_str = re.sub(r'<pre><code[^>]*>', escape_html_quotes, json_str)

    # Adım 1: content alanındaki code block'ları HTML'e çevir
    # ```...``` bloklarını <pre><code>...</code></pre> yap
    def fix_code_blocks(m):
        code = m.group(1)
        # Code block içindeki escape'leri düzelt
        code = code.replace('\\n', '\n')
        code = code.replace('\\t', '\t')
        code = code.replace('\\"', '"')
        code = code.replace('\\\\', '\\')
        # HTML entity yap
        code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        return '<pre><code>' + code + '</code></pre>'
    
    json_str = re.sub(r'```(?:\w*)\n(.*?)```', fix_code_blocks, json_str, flags=re.DOTALL)

    # Adım 2: Tüm kontrol karakterlerini temizle
    cleaned = _clean_control_chars(json_str)
    
    # Adım 3: Sondaki sorunlu karakterleri temizle
    # "}\n```" gibi durumları düzelt
    cleaned = re.sub(r'"\s*\}\s*$', '"}', cleaned)
    cleaned = re.sub(r'"\s*\]\s*$', '"]', cleaned)
    # Sondaki ```` bloklarını temizle
    cleaned = re.sub(r'```\s*$', '', cleaned)
    
    # Deneme 1: Temizlenmiş JSON (strict=False ile)
    try:
        return json.loads(cleaned, strict=False)
    except json.JSONDecodeError:
        pass

    # Deneme 2: Trailing comma düzelt
    fixed = re.sub(r',\s*([}\]])', r'\1', cleaned)
    try:
        return json.loads(fixed, strict=False)
    except json.JSONDecodeError:
        pass

    # Deneme 3: JSON bloğunu bracket balancing ile bul
    result = _extract_balanced_json(cleaned)
    if result:
        return result

    # Deneme 4: Agresif — son }'a kadar kes
    last_brace = cleaned.rfind('}')
    if last_brace > 0:
        try:
            return json.loads(cleaned[:last_brace + 1], strict=False)
        except json.JSONDecodeError:
            pass

    log.error("JSON parse hatası — tüm denemeler başarısız.")
    log.error("JSON ilk 200: %s", cleaned[:200])
    log.error("JSON son 200: %s", cleaned[-200:])
    return None


def _clean_control_chars(json_str):
    """String içindeki kontrol karakterlerini ve escape edilmemiş tırnak işaretlerini düzeltir."""
    result = []
    i = 0
    n = len(json_str)
    
    while i < n:
        ch = json_str[i]
        
        if ch == '"':
            # String başladı — sonuna kadar git
            result.append(ch)
            i += 1
            while i < n:
                ch2 = json_str[i]
                if ch2 == '\\' and i + 1 < n:
                    # Escape sequence — olduğu gibi koru
                    result.append(ch2)
                    result.append(json_str[i+1])
                    i += 2
                elif ch2 == '"':
                    # String bitti — ama önce kontrol et: bu gerçekten string sonu mu?
                    # Eğer bir sonraki karakter , veya } veya ] veya : ise, string sonudur
                    next_i = i + 1
                    while next_i < n and json_str[next_i] in ' \t\n\r':
                        next_i += 1
                    if next_i < n and json_str[next_i] in ',}]:':
                        # String sonu
                        result.append(ch2)
                        i += 1
                        break
                    else:
                        # String içinde escape edilmemiş tırnak — escape et
                        result.append('\\"')
                        i += 1
                elif ord(ch2) < 0x20:
                    # Kontrol karakteri — escape et
                    if ch2 == '\n':
                        result.append('\\n')
                    elif ch2 == '\r':
                        result.append('\\r')
                    elif ch2 == '\t':
                        result.append('\\t')
                    # Diğerlerini atla
                    i += 1
                else:
                    result.append(ch2)
                    i += 1
        else:
            result.append(ch)
            i += 1
    
    return ''.join(result)


def _extract_balanced_json(text):
    """Bracket balancing ile sağlam JSON'u çıkarır."""
    start = text.find('{')
    if start < 0:
        return None
    depth = 0
    in_string = False
    escape_next = False
    for i, ch in enumerate(text[start:], start):
        if escape_next:
            escape_next = False
            continue
        if ch == '\\' and in_string:
            escape_next = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if not in_string:
            if ch == '{':
                depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except json.JSONDecodeError:
                        return None
    return None


def estimate_read_time(html_content):
    """HTML içeriğinden tahmini okuma süresi hesaplar."""
    text = re.sub(r'<[^>]+>', '', html_content)
    words = len(text.split())
    minutes = max(1, round(words / 200))
    return f"{minutes} dk okuma"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    from dotenv import load_dotenv
    load_dotenv()

    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    test_topic = {
        "category": "Yapay Zeka",
        "title": "2026 Yılında Yapay Zeka Trendleri",
    }

    print("Makale üretiliyor...")
    article = generate_article(test_topic, config)
    if article:
        print(f"\nBaşlık: {article['title']}")
        print(f"Slug: {article['slug']}")
        print(f"Süre: {article['read_time']}")
        print(f"İçerik uzunluğu: {len(article['content'])} karakter")
    else:
        print("Makale üretilemedi!")
