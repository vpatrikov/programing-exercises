def remove_smallest(numbers):
    if not numbers:
        return numbers
    else:
        numbers_copy = numbers[:]
        numbers_copy.remove(min(numbers_copy))
        return numbers_copy