def merge_sorted_lsts(FIRST, SECOND):
    i, j = 0, 0
    result = []

    while i < len(FIRST) and j < len(SECOND):
        if FIRST[i] < SECOND[j]:
            result.append(FIRST[i])
            i += 1
        else:
            result.append(SECOND[j])
            j += 1

    if i < len(first):
        result.extend(first[i:])
    if j < len(second):
        result.extend(second[j:])
        
    return result

first = [1, 3, 5]
second = [2, 4, 6]

print("Първи списък:", first)
print("Втори списък:", second)

merged = merge_sorted_lsts(first, second)
print("Слят списък:", merged)