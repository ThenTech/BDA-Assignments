def is_unique(l):
    check = []
    unique = True
    i = 0
    while unique and i < len(l):
        if l[i] not in check:
            check.append(l[i])
            i += 1
        else:
            unique = False
    return unique
