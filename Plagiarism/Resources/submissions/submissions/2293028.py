def is_unique(l):
    unique = True
    for i in l:
        y = int(l.count(i))
        if y > 1:
            unique = False
            break
        else:
            unique = True
    return unique