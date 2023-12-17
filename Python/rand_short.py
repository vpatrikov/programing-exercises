def even_or_odd(number):
    return "Even" if (number % 2 == 0) else "Odd"

def validate_pin(pin):
    return True if pin > 0 and len(pin) == 4 or len(pin) == 6 and str(pin).isdigit else False

def double_char(s):
    return ''.join([2*x for x in s])

def get_middle(s):
    return s[(len(s)-1)//2:(len(s)+2)//2]
