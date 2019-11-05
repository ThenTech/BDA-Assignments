def shift(l, n):
    if n == 0:
        return l
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