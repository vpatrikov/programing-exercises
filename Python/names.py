def likes(names):
    namesList = list(names)
    if len(namesList) == 0:
        return "no one likes this"
    elif len(namesList) == 1:
        return f"{namesList[0]} likes this"
    elif len(namesList) == 2:
        return f"{namesList[0]} and {namesList[1]} like this"
    elif len(namesList) == 3:
        return f"{namesList[0]}, {namesList[1]} and {namesList[2]} like this"
    else:
        return f"{namesList[0]}, {namesList[1]} and {int(len(namesList - 2))} others like this"
