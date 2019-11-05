def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (gelijke_hoogte(y1,h1,y2,h2) and gelijke_horizontaal(x1,w1,x2,w2)):
        return True
    else:
        return False
def gelijke_hoogte(y1,h1,y2,h2):
    for i in range(y1,h1+y1):
        for j in range(y2,h2+y2):
            if i==j:
                return True
    return False
def gelijke_horizontaal(x1,w1,x2,w2):
    for i in range(x1,x1+w1):
        for j in range(x2,w2+x2):
            if i == j:
                return True
    return False