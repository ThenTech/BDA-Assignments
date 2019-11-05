def is_ordered(l):
    ordered = True
    i = 0
    while ordered and i < len(l)-1:
        if l[i] > l[i+1]:
            ordered = False
        i += 1
    return ordered