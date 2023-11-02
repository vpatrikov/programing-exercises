def running_average():
    total_sum = 0
    count = 0

    def average(new_value):
        nonlocal total_sum, count
        total_sum += new_value
        count += 1
        return round(total_sum / count, 2)
    return average  