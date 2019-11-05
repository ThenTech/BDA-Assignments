def shift(l, n):
    # met dit gaat ook
    copy = []
    for i in range(len(l)):
        oldi = (i-n)% len(l)
        copy.append(l[oldi]
    return copy