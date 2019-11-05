def is_unique(l):
    for i in range(len(l)):
        for j in range(i+1, len(l)-1):
            if l[i] == l[i+j]:
                return False
    return True