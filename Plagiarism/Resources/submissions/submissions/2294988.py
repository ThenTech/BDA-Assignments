def is_unique(l):
    check = True
    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if l[i] == l[j] and i != j:
                check = False
            if not check:
                break
        if not check:
            break
    if check:
        return True
    return False

