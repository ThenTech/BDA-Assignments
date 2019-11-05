def shift(l, n):
    if len(l)==0:
        return l
    n = n%len(l)
    lijst = []
    lijst += l[len(l)-n:]
    lijst += l[:len(l)-n]
    return lijst