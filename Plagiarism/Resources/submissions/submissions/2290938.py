def is_unique(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if j>i:
                if l[j] == l[i]:
                    return False
    return True
