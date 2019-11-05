def is_unique(l):
    for i in range(0, len(l)):
        for j in l[i + 1:]:
            if j == l[i]:
                return False
                
    return True