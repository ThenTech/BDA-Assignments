def is_ordered(l):
    copy = l[:]
    copy.sort()

    return copy == l
