def shift(l, n):
    newl = []
    if l == []:
        return l
    if n >= 0:
        while n > len(l):
            n -= len(l)
        for i in range(len(l)-n, len(l)):
            newl.append(l[i])
        for i in range(len(l)-n):
            newl.append(l[i])
        return newl
    if n < 0:
        while n < -len(l):
            n += len(l)
        for i in range(-n, len(l)):
            newl.append(l[i])
        for i in range(-n):
            newl.append(l[i])
        return newl