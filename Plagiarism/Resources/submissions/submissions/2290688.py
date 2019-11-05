def is_ordered(l):
    a = l[:]
    a.sort()
    if a == l:
        return True
    else:
        return False