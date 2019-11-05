def is_unique(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i] == l[j]:
                return False     
    return True