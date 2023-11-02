def last_digit(n1, n2):
    if n2 == 0:
        return 1

    last_digit_result = (n1 % 10) ** (n2 % 4 + 4)
    return last_digit_result % 10
