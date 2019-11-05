def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if ((x2 < x1 + w1) or (x2 + w2 < x1 + w1)) or ((x1 < x2 + w2 or (x1 + w1 < x2 + w2))) and ((y2 < y1 + h1) or (y2 + h2 < y1 + h1)) or ((y1 < y2 + h2 or (y1 + h1 < y2 + h2))):
        return True
    return False