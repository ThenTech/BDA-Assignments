def shift(l, n):
    while n > len(l):
        n = n - len(l)
    if n > 0:
        return l[n+1:] + l[:n+1]
    elif n < 0:
        return l[n-1:] + l[:n-1]
    else:
        return l