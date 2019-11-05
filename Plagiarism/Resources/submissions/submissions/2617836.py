def is_unique(l):
    x = True
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] == l[j] and i != j:
                x = False         
    return x