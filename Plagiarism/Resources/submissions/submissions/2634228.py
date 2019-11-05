def is_ordered(l):
    for i in range(0, len(l)):
        if i != len(l) - 1:
            if l[i] <= l[i + 1]:
                continue
            else:
                return False
    return True