def shift(l, n):
    n = n%len(l)
    lijst = []
    lijst += lijst[n:]
    lijst += lijst[:n]
    return lijst