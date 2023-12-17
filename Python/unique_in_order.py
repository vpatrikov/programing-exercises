def unique_in_order(sequence):
    unique = []
    for item in sequence:
        if not unique or item != unique[-1]:
            unique.append(item)
    return unique