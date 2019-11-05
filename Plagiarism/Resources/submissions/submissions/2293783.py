def is_unique(l):
    for i in l:
        l.count(i)
        if i != 1:
            return True
    return False