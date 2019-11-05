def is_ordered(l):
    i = 0
    while i < len(l) - 1:
        if l[i] > l[i + 1]:
            return False
        i += 1
    return True