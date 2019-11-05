def is_unique(l):
    A = l[:]
    for i in A:
        l.remove(i)
        if i in l:
            return False
    return True