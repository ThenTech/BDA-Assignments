def shift(l,n):
    copy = []
    for i in range(len(l)):
        oldi = (i - n) % len(l)
        copy.append(l[oldi])
    return copy