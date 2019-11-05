def is_ordered(l):
    k = 0
    while k < len(l) - 1:
        if l[k] > l[k + 1]:
            return False
        k += 1
    return True