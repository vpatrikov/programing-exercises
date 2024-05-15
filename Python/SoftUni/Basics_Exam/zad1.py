def get_input(name):
    validation_ranges = {
        "GPU": (1, 2000),
        "dongle": (1, 50),
        "consumed electricity per GPU": (0.01, 10),
        "profit per GPU": (1, 100)
    }

    while True:
        try:
            if name in validation_ranges and (name == "GPU" or name == "dongle"):
                price = int(input(f"Enter the price of the {name}: "))
            else:
                price = float(input(f"Enter the price of the {name}: "))

            if name in validation_ranges:
                min_val, max_val = validation_ranges[name]
                if price < min_val or price > max_val:
                    print(f"The {name} should be between {min_val} and {max_val}\n")
                    continue

            return price

        except ValueError:
            print("Input should be a number\n")

gpus_price = get_input("GPU") * 13
dongles_price = get_input("dongle") * 13

total_hardware = gpus_price + dongles_price + 1000

electricity_cost = get_input("consumed electricity per GPU")
profit_per_gpu = (get_input("profit per GPU") - electricity_cost) * 13

return_investment = int(total_hardware / profit_per_gpu)

print("Total hardware cost:", total_hardware)
print("Return on investment (in days):", return_investment)
