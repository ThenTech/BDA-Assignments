def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    outerx1 = x1 + w1
    outery1 = y1 + h1
    outerx2 = x2 + w2
    outery2 = y2 + h2
    if (outerx1 > x2 and outery1 > y2):
        return True
    return False