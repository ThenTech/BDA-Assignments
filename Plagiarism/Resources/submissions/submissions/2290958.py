def is_unique(l):
    for i in range(len(l)):
        for j in range(1, len(l)-i):
            if l[i] == l[i+j]:
                return False
    return True