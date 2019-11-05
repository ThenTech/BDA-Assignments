def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x1 + w1) <= x2:
        return False
    elif (y1 + h1) <= y2:
        return False
    else:
        return True