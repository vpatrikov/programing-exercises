def what_century(year):
    num = str((int(year) - 1) // 100 + 1)

    if num[-1] == '1' and num[-2:] != '11':
        num += "st"
    elif num[-1] == '2' and num[-2:] != '12':
        num += "nd"
    elif num[-1] == '3' and num[-2:] != '13':
        num += "rd"
    else:
        num += "th"

    return num