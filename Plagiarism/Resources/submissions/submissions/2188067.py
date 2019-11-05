def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    x = check_axes(x1, w1, x2, w2, y1, h1, y2)
    y = check_axes(y1, h1, y2, h2, x1, w1, x2)
    if x and y:
        return True
    else:
        return False


def check_axes(c1, c2, c3, c4, c5, c6, c7):
    if c1 < c3 or c1 > c3 or c1 == c3 and c5 + c6 > c7:
        return True
    else:
        return False


