def as_intersect(a, b, c, d):
    if a <= d or b >= c:
        return True
    return False

def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    # a = x1   b = x1 + w1   c = x2   d = x2 + w2

    if as_intersect(x1, x1 + w1, x2, x2 + w2) and as_intersect(y1, y1 + h1, y2, y2 + h2):
        return True
    return False