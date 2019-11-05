def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 < x2 < x1 + w1) and (y1 < y2 < y1 + h1):
        return True
    else:
        return False