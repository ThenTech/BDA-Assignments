def is_unique(l):
    for i in len(l):
        for j in [0:i, i+1:len(l)]:
            if l[i] == l[j]:
                return False
    return True