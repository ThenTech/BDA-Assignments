def is_ordered(l):
    check = True
    for i in range(0, len(l)-1):
        if l[i] > l[i+1]:
            check = False
    return check