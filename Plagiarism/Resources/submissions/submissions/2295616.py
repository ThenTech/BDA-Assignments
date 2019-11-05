def shift(l, n):
    if n >= 0:
        if n > len(l):
            z = n % len(l)
            a =(len(l))
            r = l[a-z:]
            s = l[:a-z]
            t = r + s
            return t
        else:
            a = (len(l))
            r = l[a - n:]
            s = l[:a - n]
            t = r + s
            return t
    
    else:
        a = (len(l)) + n
        r = l[n-1:]
        s = l[:n-1]
        t = r + s
        return t