with open("last_failed_response.txt", "r", encoding="utf-8") as f:
    text = f.read()

import re, json

# JSON bloğunu bul
m = re.search(r'\{', text)
if m:
    json_str = text[m.start():]
    print(f"Uzunluk: {len(json_str)}")
    print()
    
    # Control char ara
    for i, ch in enumerate(json_str):
        if ord(ch) < 32 and ch not in '\n\r\t':
            print(f"CONTROL CHAR at pos {i}: ord={ord(ch)} hex=0x{ord(ch):02x}")
            print(f"  Context: ...{json_str[max(0,i-20):i+20]}...")
    
    # Bracket derinliği
    in_string = False
    escape = False
    depth = 0
    for i, ch in enumerate(json_str):
        if escape:
            escape = False
            continue
        if ch == '\\' and in_string:
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if not in_string:
            if ch == '{': depth += 1
            elif ch == '}': depth -= 1
    print(f"\nFinal bracket depth: {depth}")
    
    # String içindeki yeni satırları bul
    in_string = False
    escape = False
    newlines_in_strings = []
    for i, ch in enumerate(json_str):
        if escape:
            escape = False
            continue
        if ch == '\\' and in_string:
            escape = True
            continue
        if ch == '"':
            in_string = not in_string
            continue
        if in_string and ch == '\n':
            newlines_in_strings.append(i)
    
    if newlines_in_strings:
        print(f"\nString içinde {len(newlines_in_strings)} yeni satır bulundu!")
        for pos in newlines_in_strings[:5]:
            print(f"  Pos {pos}: ...{json_str[max(0,pos-30):pos+30]}...")
    else:
        print("\nString içinde yeni satır yok.")
