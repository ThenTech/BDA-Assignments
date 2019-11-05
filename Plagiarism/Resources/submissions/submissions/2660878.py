def shift(l, n):
    n = n%len(l)
    lijst = []
    lijst += l[len(l)-n-1:]
    lijst += l[:len(l)-n-1]
    return lijst