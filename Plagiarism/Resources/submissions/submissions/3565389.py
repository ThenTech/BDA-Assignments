def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 + h1) > y2 and w2 > 0:
        return True
    return False