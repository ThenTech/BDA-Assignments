def shift(l, n):
    if 0 < n < 10:
        n += 1
    elif n < 0 or n >= 10:
        n -= 1
    if not l:
        return []
    n %= len(l)
    return l[n:] + l[:n]