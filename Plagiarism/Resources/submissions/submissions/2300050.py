def is_unique(l):
    check = []
    for i in l:
        if i not in check:
            check.append(i)
        else:
            return False
    return True