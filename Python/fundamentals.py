def multiply(n):
    return n * 5**len(str(abs(n)))

def to_alternating_case(string):
    result = []
    for char in string:
        if char.islower():
            result.append(char.upper())
        else:
            result.append(char.lower())
    return ''.join(result)
