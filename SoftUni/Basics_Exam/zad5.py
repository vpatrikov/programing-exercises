while True:
    try:
        food_amount = int(input())
        if food_amount < 1 or food_amount > 100:
            print("The amount of food should be in kg and between 1 and 100\n")
            continue
        else:    
            food_amount *= 1000
        break
    except ValueError:
        print("Input should be int")

input_value = None
sum_of_food = 0

while input_value != "Adopted":
    try:
        input_value = input()
        if input_value != "Adopted":
            if int(input_value) < 1 or int(input_value) > 1000:
                print("Number out of range (1 to 1000)")
                continue
            else:
                input_value = int(input_value)
    except ValueError:
        print("Please enter a valid number or 'Adopted'.")
        continue
    else:
        if type(input_value) is not str:
            sum_of_food += input_value

if sum_of_food > food_amount:
    print(f"Food is not enough. You need {sum_of_food - food_amount} grams more.")
else:
    print(f"Food is enough! Leftovers: {food_amount - sum_of_food}")



