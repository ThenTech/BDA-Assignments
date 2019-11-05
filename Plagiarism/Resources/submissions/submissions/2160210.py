def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    x1 = int (x1)
    x2 = int (x2)
    y1 = int (y1)
    y2 = int (y2)
    w1 = int (w1)
    w2 = int (w2)
    h1 = int (h1)
    h2 = int (h2)
    
        
    xb = x2-x1
    yb = y2-y1
    if xb<=w1 and xb=>w2 and yb<=h1 and yb=>h2:
        return True
    else:
        return False