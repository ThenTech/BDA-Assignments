def shift(l, n):
    if len(l)==0:
        return l
    if n > 2*len(l):
        p = (n % len(l))
        a = l[0:((len(l)) - p)]
        y = l[((len(l)) - p):len(l)]

        b = l[0: (p * (-1))]
        z = l[p * (-1):]
        if p < 0:
            x = z + b
        else:
            x = y + a
    else:
        a = l[0:((len(l))-n)]
        y = l[((len(l))-n):len(l)]

        b = l[0: (n*(-1))]
        z = l[n*(-1):]
        if n < 0:
            x = z+b
        else:
            x = y+a

    return x
shift([4], 13)







shift([1, 2, 3, 4, 5], 2)