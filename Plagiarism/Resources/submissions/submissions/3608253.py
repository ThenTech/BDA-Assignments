def shift(l, n):
    if len(l) == 0:
        return l
    
    while n < len(l)*(-1):
        n += len(l)
    while n >= len(l):
        n -= len(l)
    
    if n < 0:
        for i in range(abs(n)):
            getal = l[0]
            l.remove(getal)
            l.insert(len(l), getal)
    if n > 0:
        for i in range(n):
            getal = l[len(l)-1]
            l.remove(l[len(l)-1])
            l.insert(0, getal)
    return l