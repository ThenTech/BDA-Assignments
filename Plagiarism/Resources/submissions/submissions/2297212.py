def shift(l, n):
    a = l[0:((len(l))-n)]
    y = l[((len(l))-n):len(l)]

    b = l[0: (n*(-1))]
    z = l[n*(-1):]
    if n < 0:
        x = z+b
    else:
        x = y+a

    return x







shift([1, 2, 3, 4, 5], 2)