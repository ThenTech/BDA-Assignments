def is_ordered(l):
    sorteerd = l[:]
    sorteerd.sort()
    print("l", l)
    print("sorteer", sorteerd)
    if l == sorteerd:
        return True
    else:
        return False