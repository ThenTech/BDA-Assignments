def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 + w1) > y2 and w2 > 0 and y1 < (y2 + h2) < (y1 + h1):
        return True
    return False