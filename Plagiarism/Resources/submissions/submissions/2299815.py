def is_unique(l):
    check = []
    for i in range(1, len(l)):
        if l[i] not in check:
            check.append(i)
        else:
            return False
    return True