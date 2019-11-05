def shift(l, n):
    nieuw = []
    for i in l:
        pos = i+n
        while pos > len(l):
            pos -= len(l)
        nieuw.append(l[pos])
    return nieuw