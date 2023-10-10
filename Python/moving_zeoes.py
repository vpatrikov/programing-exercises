moveZeroes = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]

non_zero_elements = [x for x in moveZeroes if x != 0]

num_zeroes = len(moveZeroes) - len(non_zero_elements)

non_zero_elements.extend([0] * num_zeroes)

print(non_zero_elements)