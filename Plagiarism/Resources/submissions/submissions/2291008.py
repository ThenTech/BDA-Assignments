def is_ordered(l):
    for number in range(len(l) - 1):
        if l[number] > l[number + 1]:
            return False
    return True