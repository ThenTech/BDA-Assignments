def is_unique(l):
    for i in l:
        if l[l.index(i):].index(i)!=-1:
            return False
    return True