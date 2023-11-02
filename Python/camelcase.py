import re

def to_camel_case(text):
    list = re.split(r'[-_]', text)
    text_2 = (''.join(list))
    
    if text[0] == text[0].lower():
        temp = text_2[0].lower()
        text_2.replace(text_2[0], temp, 1)
    return text_2

print(to_camel_case("The_Stealth_Warrior"))

# 