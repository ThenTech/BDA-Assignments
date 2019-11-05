def shift(list, base):
    if len(list) == 0:
        return list

    if base > len(list):
        base = base - ((base % len(list) + 1)* len(list))

    if base > 0:
        firstPart = list[:base + 1]
        lastPart = list[base + 1:]
    elif base < 0:
        firstPart = list[:len(list) + base - 1]
        lastPart = list[len(list) + base - 1:]
    else:
        return list
    return lastPart + firstPart