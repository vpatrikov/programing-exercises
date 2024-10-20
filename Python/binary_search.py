from random import randint


def binary_search(list, target):
    print("Binary search:")
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = int(low + (high - low) / 2)
        value = list[middle]
       
        if value < target:
            low = middle + 1
        elif value > target:
            high = middle - 1
        else:
            return middle


rand_list = [x for x in range(100)]
print(binary_search(rand_list, 31))
