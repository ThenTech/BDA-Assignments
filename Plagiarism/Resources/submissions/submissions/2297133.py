def shift(l, n):
    l1 = []
    for i in range(0, len(l)):
        while n not in range(0, len(l)):
            if n <= 0:
                n += len(l)
            else:
                n -= len(l)
        plaats = i - n
        if plaats < len(l):
            lel = l[plaats]
            l1.append(lel)
        else:
            plaats -= len(l)
            lel = l[plaats]
            l1.append(lel)
    return l1