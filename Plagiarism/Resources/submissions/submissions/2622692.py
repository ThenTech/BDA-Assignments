def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    return lineintersect(x1,w1,x2,w2) and lineintersect(y1,h1,y2,h2)
        
def lineintersect(punt1,lengte1,punt2,lengte2):
    beginpunt = max(punt1, punt2)
    kortstelengte = min(punt1+lengte1, punt2+lengte2) 
    if beginpunt < kortstelengte:
        return True
    else:
        return False