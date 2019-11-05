def project_axis(c1, d1, c2, d2):
    if c1 > c2 and c1 < c2+d2: return True
    elif c1+d1 > c2 and c1+d1 < c2+d2: return True
    elif c2 > c1 and c2 < c1+d1: return True
    elif c2+d2 > c1 and c2+d2 < c1+d1: return True
    else: return False

def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    return project_axis(x1,w1,x2,w2) and project_axis(y1,h1,y2,h2)