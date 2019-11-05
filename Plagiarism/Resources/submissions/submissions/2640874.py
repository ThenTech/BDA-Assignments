def is_ordered(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True