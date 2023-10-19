def camel_case(s):
    list = s.split()

    for i  in range(len(list)):
        list[i] = list[i].capitalize()

    s = ''.join(list)
    
    return s;