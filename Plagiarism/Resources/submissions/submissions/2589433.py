def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 >= x1 + w1 and w2 >= 0:
        return False
    if y2 >= y1 + h1 and h2 >= 0:
        return False
    if x2 <= x1 + w1 and w2 <= 0:
        return False
    if y2 <= y1 + h1 and h2 <= 0:
        return False
    return True
        