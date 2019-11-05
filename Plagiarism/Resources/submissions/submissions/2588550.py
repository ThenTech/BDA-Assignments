def is_unique(l):
    check = []
    i = 0
    while i < len(l):
        if l[i] in check:
            return False
        check.append(l[i])
        i += 1
    return True