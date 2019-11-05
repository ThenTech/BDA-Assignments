def is_unique(l):
    for i in l:
        aantal=l.count(i)
        if aantal != 1:
            return False
    return True