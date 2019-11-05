def shift(l, n):
    newlist = [0 for x in range(len(l))]
    for i in range(len(l)):
        if i+n >= 0:
            n %= len(l)
            if i < len(l):
                newlist[i+n+1] = l[i]
            elif i >= len(l):
                newlist[i+n+1] = l[i-len(l)]
        if i+n < 0:
            n %= -len(l)
            if i >= 0:
                newlist[i+n+1] = l[i]
            elif i < 0:
                newlist[i+n+1] = l[i+len(l)]
        
    return newlist