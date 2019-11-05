def shift(l, n):
    n = n%len(l)
    lijst = []
    lijst += l[n:]
    lijst += l[:n]
    return lijst