def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    x = check_axes(x1, w1, x2, w2)
    y = check_axes(y1, h1, y2, h2)
    if x1 == x2 and y1 + h1 > y2 or x1 == x2 and y2+ h2 > y1:
        return True
    if x and y:
        return True
    else:
        return False


def check_axes(c1, c2, c3, c4):
    if c1 < c3 and c1+c2 <= c3+c4 or c1 > c3 and c1+c2 >= c3+c4 or c1<c3 and c1+c2 > c3+c4 or c1 > c3 and c3+c4 > c1+c2:
        return True
    else:

        return False