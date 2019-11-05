def is_unique(l):
    unique = True
    for i in range(0, len(l)):
        for j in l[i+1:]:
            if l[i] != j:
                continue
            else:
                unique = False
                break
        if not unique:
            break
    return unique