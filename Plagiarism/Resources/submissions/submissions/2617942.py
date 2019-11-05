def shift(l, n):
    while n > len(l):
        n -= len(l)
    while n < (-len(l)):
        n += len(l)

    if n > 0:
        l =l[len(l)-n:] + l[:len(l)-n]
    if n < 0:
        l = l[(-n):] + l[:(-n)]

    return l