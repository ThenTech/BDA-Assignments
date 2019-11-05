def is_unique(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] == l[j]:
                return False
            else:
                continue
    return True