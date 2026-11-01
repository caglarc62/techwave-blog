# -*- coding: utf-8 -*-
"""1 Kasım makalesini search-index.json'a ekler (idempotent)."""
import io, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
p = os.path.join(BASE, "search-index.json")
with io.open(p, encoding="utf-8") as f:
    data = json.load(f)

data = [x for x in data if x.get("s") != "yapay-zeka-ajani-mcp-guvenlik-rehberi"]

entry = {
    "t": "Yapay Zekâ Ajanları ve MCP: Araç Bağlantılarının Güvenliği",
    "s": "yapay-zeka-ajani-mcp-guvenlik-rehberi",
    "c": "Yapay Zeka",
    "e": "Ajanlar dosya, veritabanı ve e-postaya dokunuyor. Prompt injection, en az yetki ve onay akışıyla güvenli kurulum rehberi.",
    "d": "1 Kasım 2026",
    "i": "https://techwaveblog.site/images/mcp-guvenlik-2026-1.svg",
    "h": (
        "Yapay Zekâ Ajanları ve MCP: Araç Bağlantılarının Güvenliği | "
        "1. MCP tam olarak ne yapıyor? | "
        "2. Birinci tehdit: Prompt injection | "
        "3. İkinci tehdit: Yetki aşımı ve yanlış hedef | "
        "4. Üçüncü tehdit: Denetimsizlik | "
        "5. Güvenli ajan kurulumu: 6 ilke | "
        "6. Kurumsal kontrol listesi | "
        "7. Sıkça Sorulan Sorular | "
        "8. Sonuç"
    ),
    "x": (
        "Yapay zekâ ajanları artık sadece metin üretmiyor; dosya okuyor, veritabanına yazıyor, "
        "e-posta gönderiyor ve web’de geziniyor. Model Context Protocol (MCP) bu araçları tek bir "
        "standard üzerinden modele bağlamayı kolaylaştırıyor. Aynı kolaylık, kötü niyetli bir girdinin "
        "tek bir komutla gerçek bir zarara dönüşmesi demek."
    ),
}

data.insert(0, entry)
with io.open(p, "w", encoding="utf-8") as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=None))
print("search-index.json guncellendi")
