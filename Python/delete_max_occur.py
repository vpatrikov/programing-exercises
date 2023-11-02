def limit_repetition(input_list, N):
    result = []
    count_dict = {}

    for item in input_list:
        if item in count_dict:
            if count_dict[item] < N:
                result.append(item)
                count_dict[item] += 1
        else:
            result.append(item)
            count_dict[item] = 1

    return result

# Example usage:
input_list1 = [1, 2, 3, 1, 2, 1, 2, 3]
N1 = 2
result1 = limit_repetition(input_list1, N1)
print(result1)  # Output: [1, 2, 3, 1, 2, 3]

input_list2 = [20, 37, 20, 21]
N2 = 1
result2 = limit_repetition(input_list2, N2)
print(result2)  # Output: [20, 37, 21]
