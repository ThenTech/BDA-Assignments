def is_unique(l):
    for i in l:
        if l.count(i)>1:
            return False
    return True