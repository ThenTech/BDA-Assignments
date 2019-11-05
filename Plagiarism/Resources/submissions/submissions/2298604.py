def shift(l, n):
    k = l + []
    for i in range(len(l)):
        if i+n < 0:
            k[i] = l[len(l)+1+i+n]
        elif i+n > len(l):
            k[i] = l[i+n-len(l)-1]
        else:
            k[i] = l[i+n]
    return k