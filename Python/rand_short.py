def even_or_odd(number):
    return "Even" if (number % 2 == 0) else "Odd"

def validate_pin(pin):
    return True if pin > 0 and len(pin) == 4 or len(pin) == 6 and str(pin).isdigit else False