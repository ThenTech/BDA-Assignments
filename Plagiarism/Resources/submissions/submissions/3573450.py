def rotate(l):
    list = []
    for i in range(1, len(l)+1):
        if i == len(l):
            list.append(l[0])
        else:
            list.append(l[i])
    return list
    
def shift(l, n):
    if len(l) == 0:
        return []
    while n > len(l):
        n -= len(l)
    while n < (len(l)*(-1)):
        n += len(l)
    if n > 0:
        n = len(l) - n
    for i in range(abs(n)):
        l = rotate(l)
    return l