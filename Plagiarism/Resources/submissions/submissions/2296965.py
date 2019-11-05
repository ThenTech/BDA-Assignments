def shift(l, n):
    if n>=0:
        n %= len(l)
        return l[len(l)-n:] + l[:len(l)-n]
    elif n<0:
        n %= -len(l)
        return l[-n:] + l[:-n]