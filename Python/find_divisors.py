def divisors(integer):
    listNums = []
    for i in range(2, integer + 1):
        if i > 0 and integer % i == 0:
            listNums.append(i)
            
    if integer == listNums[0]:
        return f"{integer} is prime"
    elif listNums[-1] == integer:
        listNums.pop()
        return listNums
        

print(divisors(25))
