def is_ordered(l):
    a = l[:]
    a.sort()
    print(a)
    if a == l:
        return True
    else:
        return False