def is_unique(l):
    x = len(l)-1
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[i] == l[x-j]:
                return False
    return True