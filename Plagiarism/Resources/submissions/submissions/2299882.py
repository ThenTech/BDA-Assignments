def is_unique(l):
    check = []
    for i in range(len(l)):
        if l[i] not in check:
            check.append(l[i])
        else:
            return False
    return True