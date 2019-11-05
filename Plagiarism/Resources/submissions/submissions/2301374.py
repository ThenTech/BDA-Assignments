def is_unique(l):
    for x in range(len(l)-1):
        for y in range(x+1, len(l)):
            if l[y]==l[y]:
                return False
    return True