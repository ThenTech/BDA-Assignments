def is_unique(l):
    unique = l[:]
    unique.count(l)
    if unique.count(l) != 1:
        False
    else:
        True