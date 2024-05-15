while True:
    try:
        cats_amount = int(input())
        break
    except ValueError:
        print("Input should be integer.")

group_1 = group_2 = group_3 = 0
sum_food_kg = 0

for i in range (cats_amount):
    while True:
        try:
            cat_food = float(input())
            if cat_food >= 100 and cat_food < 200:
                group_1 += 1
            elif cat_food >= 200 and cat_food < 300:
                group_2 += 1
            elif cat_food >= 300 and cat_food < 400:
                group_3 += 1
            else:
                print("Invalid food size (min is 100, max is 399)")
                continue
            sum_food_kg += cat_food
            break
        except ValueError:
            print("Input should be float")

sum_food_kg /= 1000

price_total_food = round(sum_food_kg * 12.45, 2)

print(f"Group 1: {group_1} cats")
print(f"Group 2: {group_2} cats")
print(f"Group 3: {group_3} cats")
print(f"Price for food per day: {price_total_food} leva")