def is_unique(l):
    for i in l:
        if l[l.find(i):].find(i)!=-1:
            return False
    return True