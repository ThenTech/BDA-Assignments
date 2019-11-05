def is_unique(l):
    lengte = len(l)
    for i in range(len(l)):
        y = l[i]
        for j in range(len(l)):
            if y == l[j]:
                return False
    return True