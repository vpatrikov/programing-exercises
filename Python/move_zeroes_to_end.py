def move_zeros(lst):
    for i in range(len(lst)):
        if lst[i] == 0:
            lst.append(lst[i])
            lst.remove(lst[i])
    return lst