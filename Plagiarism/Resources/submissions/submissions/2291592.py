def shift(list, base):
    if base > 0:
        firstPart = list[:base + 1]
        lastPart = list[base + 1:]
    else:
        firstPart = list[:len(list) + base - 1]
        lastPart = list[len(list) + base - 1:]
    return lastPart + firstPart