def is_ordered(l):
    lengte = len(l)
    for i in range(1,lengte):
        if l[i-1] > l[i]:
            return False
        else:
            return True
            