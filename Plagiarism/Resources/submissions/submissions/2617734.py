def is_ordered(l):
    x = True
    for i in range(len(l)-1):
            if l[i+1] < l[i]:
                x = False
    return x