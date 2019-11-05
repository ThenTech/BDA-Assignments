def is_unique(l):
    for x in range(len(l)-1):
        for y in x:
            if x[y] == l[x]:
               return False 
