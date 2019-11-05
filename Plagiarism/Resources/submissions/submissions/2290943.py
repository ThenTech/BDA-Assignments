def is_ordered(l):
    sorteerd = l[:]
    sorteerd.sort()
    if l == sorteerd:
        return True
    else:
        return False