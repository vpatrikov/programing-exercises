def digital_root(n):
    numberList = [int(x) for x in str(n)]
    sum_2 = 0

    if sum(numberList) >= 10 and sum(numberList) < 1000:
        sumList = [int(x) for x in str(sum(numberList))]
        sum_2 = sum(sumList)
        while sum_2 >= 10:
            listcon = [int(x) for x in str(sum_2)]
            sum_2 = sum(listcon)

        return sum_2
    else:
        return sum(numberList)

print(digital_root(8768214544699))

