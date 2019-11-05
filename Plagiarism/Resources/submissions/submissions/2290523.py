def is_unique(l):
    for i in range(len(l)):
        if l[i] in l[i+1:]:
            return False
    return True