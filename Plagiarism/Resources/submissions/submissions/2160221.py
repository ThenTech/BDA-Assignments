def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 < x2 and y1 < y2 and (x1+w1 > x2 or y1+h1 > y2):
        return True
    if x2 < x1 and y2 < y1 and (x2+w2 > x1 or y2+h2 > y1):
        return True
    return False