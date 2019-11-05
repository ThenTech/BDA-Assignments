def shift(l, n):
    lengte = len(l)
    l_new = []
    if lengte <1:
        return l
    if n > 0:
        n = n%(lengte)
        for j in range(1,n+1):
           x = l[lengte - 1 -n+j]
           l_new.append(x)
        for i in range(lengte-n):
          l_new.append(l[i])
        return l_new
    elif n < 0:
        n = -((-n)%(lengte-1))
        for i in range(lengte+n):
            l_new.append(l[i+n-1])
        for j in range((-1*n)):
            x = l[j]
            l_new.append(x)
        return l_new
    else:
        return l