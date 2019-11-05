def is_unique(l):
    lengte = len(l)
    for i in range(len(l)):
        new_l = l[:]
        y = l[i]
        del new_l[i]
        for j in range(len(l)-1):
            x = new_l[j]
            if y == x:
                return False
    return True