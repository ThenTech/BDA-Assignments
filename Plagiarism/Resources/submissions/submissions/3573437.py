def rotate(l):
    for i in range(1, len(l)):
        if i == len(l)-1:
            l[0] = l[i]
        else:
            l[i-1] = l[i]
    return l
    
def shift(l, n):
    while n > len(l):
        n -= len(l)
    while n < (len(l)*(-1)):
        n += len(l)
    if n < 0:
        n = len(l) + n
    for i in range(n):
        l = rotate(l)
    return l