def is_unique(l):
    for i in l:
        print(i)
        for j in l:
            if i != j:
                if l[i-1] == l[j-1]:
                    return False
            print(j)