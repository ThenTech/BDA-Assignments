def shift(l, n):
    return l[len(l)-n:] + l[:len(l)-n]