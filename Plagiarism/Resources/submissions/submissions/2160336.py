def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 < x2 and y1 < y2 and x1+w1 > x2 and y1+h1 > y2:
        return True
    if y1 < y2 and y1+h1 > y2 and (x1>=x2 and x1+w1<=x2 or x1<=x2 and x1+w1>=x2):
        return True
        
    x3 = x1 
    y3 = y1
    w3 = w1
    h3 = h1
    
    x1 = x2
    y1 = y2
    w1 = w2
    h1 = h2
    
    x2 = x3
    y2 = y3
    w2 = w3
    h2 = h3
    
    if x1 < x2 and y1 < y2 and x1+w1 > x2 and y1+h1 > y2:
        return True
    if y1 < y2 and y1+h1 > y2 and (x1>=x2 and x1+w1<=x2 or x1<=x2 and x1+w1>=x2):
        return True
        
    return False
    
    return False