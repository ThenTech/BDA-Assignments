def shift(l, n):
    nieuw = []
    for i in l:
        nieuw.append(l[i+n])
    return nieuw