import os
import glob

articles_dir = os.path.join(os.path.dirname(__file__), "articles")

# Common mojibake replacements for UTF-8 interpreted as Latin-1
MOJIBAKE = {
    'Ã¶': 'ö', 'Ã¼': 'ü', 'ÅŸ': 'ş', 'Ä±': 'ı', 'Ã‡': 'Ç', 'ÄŸ': 'ğ',
    'Ãœ': 'Ü', 'Ã–': 'Ö', 'Ã®': 'î', 'Ã¡': 'á', 'Ã ': 'à', 'Ã¤': 'ä',
    'Â»': '»', 'Â«': '«', 'â€"': '—', 'â€"': '–', 'â€˜': ''', 'â€™': ''',
    'â€œ': '"', 'â€\x9d': '"', 'Ã¢': 'â', 'Ã¨': 'è', 'Ã©': 'é',
    'Ã¨': 'è', 'Ãª': 'ê', 'Ã«': 'ë', 'Ã¬': 'ì', 'Ã­': 'í',
    'Ã®': 'î', 'Ã¯': 'ï', 'Ã°': 'ð', 'Ã±': 'ñ', 'Ã²': 'ò',
    'Ã³': 'ó', 'Ã´': 'ô', 'Ãµ': 'õ', 'Ã·': '÷', 'Ã¸': 'ø',
    'Ã¹': 'ù', 'Ãº': 'ú', 'Ã»': 'û', 'Ã½': 'ý', 'Ã¿': 'ÿ',
    'Ã\x81': 'Á', 'Ã\x82': 'Â', 'Ã\x83': 'Ã', 'Ã\x84': 'Ä',
    'Ã\x85': 'Å', 'Ã\x86': 'Æ', 'Ã\x87': 'Ç', 'Ã\x88': 'È',
    'Ã\x89': 'É', 'Ã\x8a': 'Ê', 'Ã\x8b': 'Ë', 'Ã\x8c': 'Ì',
    'Ã\x8d': 'Í', 'Ã\x8e': 'Î', 'Ã\x8f': 'Ï', 'Ã\x90': 'Ð',
    'Ã\x91': 'Ñ', 'Ã\x92': 'Ò', 'Ã\x93': 'Ó', 'Ã\x94': 'Ô',
    'Ã\x95': 'Õ', 'Ã\x96': 'Ö', 'Ã\x97': '×', 'Ã\x98': 'Ø',
    'Ã\x99': 'Ù', 'Ã\x9a': 'Ú', 'Ã\x9b': 'Û', 'Ã\x9c': 'Ü',
    'Ã\x9d': 'Ý', 'Ã\x9e': 'Þ', 'Ã\x9f': 'ß',
    'Ã\xa0': ' ', 'Ã¡': '¡', 'Ã¢': '¢', 'Ã£': '£', 'Ã¤': '¤',
    'Ã¥': '¥', 'Ã¦': '¦', 'Ã§': '§', 'Ã¨': '¨', 'Ã©': '©',
    'Ãª': 'ª', 'Ã«': '«', 'Ã¬': '¬', 'Ã\xad': '­', 'Ã®': '®',
    'Ã¯': '¯', 'Ã°': '°', 'Ã±': '±', 'Ã²': '²', 'Ã³': '³',
    'Ã´': '´', 'Ãµ': 'µ', 'Ã¶': '¶', 'Ã·': '·', 'Ã¸': '¸',
    'Ã¹': '¹', 'Ãº': 'º', 'Ã»': '»', 'Ã¼': '¼', 'Ã½': '½',
    'Ã¾': '¾', 'Ã¿': '¿',
    # Turkish specific
    'Ã–': 'Ö', 'Ã¼': 'ü', 'Ã§': 'ç', 'Ä±': 'ı', 'ÅŸ': 'ş',
    'Ä\x9e': 'Ğ', 'Ä\x9f': 'ğ', 'Ãœ': 'Ü', 'Ã‡': 'Ç',
    'Ã\x87': 'Ç', 'Ã¶': 'ö',
    # More patterns
    'Ã': 'A', 'Â': '', 'â‚¬': '€',
}

for filepath in glob.glob(os.path.join(articles_dir, "*.html")):
    with open(filepath, 'rb') as f:
        raw = f.read()
    
    # Try to decode as UTF-8
    try:
        text = raw.decode('utf-8')
    except:
        try:
            text = raw.decode('latin-1')
        except:
            continue
    
    # Check if it has mojibake
    has_mojibake = False
    for key in MOJIBAKE:
        if key in text:
            has_mojibake = True
            break
    
    if has_mojibake:
        for bad, good in MOJIBAKE.items():
            text = text.replace(bad, good)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Fixed: {os.path.basename(filepath)}")
    else:
        print(f"OK: {os.path.basename(filepath)}")
