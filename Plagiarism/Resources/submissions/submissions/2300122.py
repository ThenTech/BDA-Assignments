def is_unique(l):
    for i in range(l):
        if l[l.find(i):].find(i)!=-1:
            return False
    return True