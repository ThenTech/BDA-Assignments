def shift(l, n):
    l1 = []
    for i in range(0, len(l)):
        plaats = i - n
        if i - n > len(l):
            plaats -= n
        if plaats < len(l):
            lel = l[plaats]
            l1.append(lel)
        else:
            plaats -= len(l)
            lel = l[plaats]
            l1.append(lel)
    return l1