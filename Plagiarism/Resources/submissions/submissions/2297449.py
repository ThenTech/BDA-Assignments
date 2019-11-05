def is_unique(l):
    for x in l:
        l.count(x)
    if l.count(x) < 2:
        return
