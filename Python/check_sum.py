number = input("Enter a number")
numberSum = []
sum = 0

for digit in str(number):
    temp = int(digit)*int(digit)
    numberSum.append(temp)
    sum += temp;

if number == sum:
    print (True)
else:
    print (False)