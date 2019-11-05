def shift(l, n):
    if n>=0:
        return l[len(l)-n:] + l[:len(l)-n]
    elif n<0:
        return l[-n:] + l[:-n]