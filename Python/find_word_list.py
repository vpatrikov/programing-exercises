def find_needle(haystack):
    position = 0
    for i in range(1, len(haystack)):
        if haystack[i] == "needle":
            position = i
            break
    return f"found the needle at position {position}"
        