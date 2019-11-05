def is_unique(l):
    unique = True
    for i in l:
        l.count(l)
        if l > 1:
            unique = False
        else:
            unique = True
    return unique