def camel_case(s):
    list = s.split()

    for item in list:
        item.capitalize()

    s = str(list)
    for i in range(len(s)):
        if s[i] == ' ':
            s.replace(s[i], '')
    return s;
