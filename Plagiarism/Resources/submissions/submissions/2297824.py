def is_unique(l):
    for i in len(l):
        for j in range(0:i, i:len(l)):
            if l[i] == l[j]:
                return False
    return True