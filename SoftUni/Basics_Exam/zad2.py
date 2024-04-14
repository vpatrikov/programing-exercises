from math import ceil

def get_input(name):
    while True:
        try:
            if name == "budget":
                value = float(input())
            elif name in ["bottles count", "chips count"]:
                value = int(input())
            else:
                return "ERROR: Undefined 'name' in get_input function"
        except ValueError:
            if name == "budget":
                print("Input should be float\n")
            else:
                print("Input should be int\n")
        return value

name = input()

budget = get_input("budget")
amount_bottles = get_input("bottles count")
amount_chips = get_input("chips count")

beer_price = 1.20 * amount_bottles
chips_price = ceil(0.45 * beer_price * amount_chips)

total_spent = beer_price + chips_price

if total_spent <= budget:
    print(f"{name} bought a snack and has {round(budget - total_spent, 2)} leva left.\n")
else:
    print(f"{name} needs {round(total_spent - budget, 2)} more leva!\n")