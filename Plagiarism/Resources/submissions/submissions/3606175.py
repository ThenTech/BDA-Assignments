def is_ordered(l):
    ordered = True
    i = 0
    while i < len(l) - 1:
        if not (l[i] <= l[i+1]):
            return False
        i += 1
    return ordered