def shift(l, n):
    nieuw = []
    for i in l:
        pos = i+n
        while pos > len(l):
            pos -= len(l)
        while pos < 0:
            pos += len(l)
        nieuw.append(l[pos])
    return nieuw