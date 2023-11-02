def reverse_words(s):
    x = list(s.split())
    x.reverse()
    return ' '.join(x)

print(reverse_words("Hello World"))
