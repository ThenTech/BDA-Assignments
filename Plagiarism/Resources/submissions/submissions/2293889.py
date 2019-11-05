def is_ordered(l):
    check = True
    for i in range(0,len(l)):
        if l[i] > l[i+1]:
            check = False
    return check