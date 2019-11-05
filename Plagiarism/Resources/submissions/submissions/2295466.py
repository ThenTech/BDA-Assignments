def shift(l, n):
    if n >= 0:
        a =(len(l))
        r = l[a-n:]
        s = l[:a-n]
        t = r + s
        return t
    else:
        a = (len(l)) + n
        r = l[n-1:]
        s = l[:n-1]
        t = r + s
        return t