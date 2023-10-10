def narcissistic_num(a):
    sum, temp = 0, 0;

    digit_list = [int(digit) for digit in str(a)]

    for digit in digit_list:
        temp = digit ** len(str(a))
        sum += temp;

    return a == sum

print(narcissistic_num(153))
print(narcissistic_num(153819084))

