def is_unique(l):
    lengte = len(l)
    for i in range(len(l)):
        x = l.find(l[i])
        if x != -1:
            return False
    return True