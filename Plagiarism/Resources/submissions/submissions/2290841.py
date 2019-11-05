def is_unique(l):
    for i in range(l):
        for j in range(l):
            if j>i:
                if l[j] == l[i]:
                    return False
    return True