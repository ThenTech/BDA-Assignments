def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    return bool(x1 + w1 < x2 + w2 or y1 + h1 < y2 + h2)
