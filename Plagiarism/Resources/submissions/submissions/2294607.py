def shift(l, n):
    if n > 0:
        return l[n+1:] + l[:n+1]
    elif n < 0:
        return l[n - 1:] + l[:n - 1]
    else:
        return l