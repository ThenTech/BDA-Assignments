def shift(l, n):
    nieuw = []
    teller = 0
    for i in l:
        pos = teller+n
        while pos > len(l):
            pos -= len(l)
        while pos < 0:
            pos += len(l)
        nieuw.append(l[pos])
        teller += 1
    return nieuw