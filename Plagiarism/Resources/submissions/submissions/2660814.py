def shift(l, n):
    n = n%len(l)
    lijst = []
    lijst += l[n-1:]
    lijst += l[:n-1]
    return lijst