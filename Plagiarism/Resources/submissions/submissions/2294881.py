def shift(l, n):
    if n > 0:
        n += 1
    if n < 0:
        n -= 1
    n = n % len(l)
    return l[n:] + l[:n]