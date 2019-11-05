def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 > x2+w2 or x2 > x1+w1:
        return False

    if y1 > y2+h2 or y2 > y1+h1:
        return False

    return True