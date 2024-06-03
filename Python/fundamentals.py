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

def removing_elemets(my_list):
    return my_list[1::2]

def sort_by_length(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


