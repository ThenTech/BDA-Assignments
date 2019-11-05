def is_unique(l):
    for i in l:
        for j in l:
            if i != j:
                if j <= len(l) and i <= len(l):
                    if l[i] == l[j]:
                        return False
    return True