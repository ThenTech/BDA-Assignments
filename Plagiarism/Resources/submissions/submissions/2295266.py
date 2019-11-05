def shift(l, n):
    if l != []:
        while n > len(l):
            n -= len(l)
        if n > 0:
            return l[-n:] + l[:-n]
        elif n < 0:
            return l[-n:] + l[:-n]
        return l
    else:
        return []