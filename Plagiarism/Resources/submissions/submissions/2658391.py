def is_unique(l):
    x = True
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j:
                if l[i] = l[j]:
                    x = False
                