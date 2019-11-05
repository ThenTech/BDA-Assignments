def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 < x1:
        x = x1
        x1 = x2
        x2 = x
        w1 = w2
    if y2 < y1:
        y = y1
        y1 = y2
        y2 = y
        h1 = h2
    if x2 != x1 + h1 or y2 != y1 + w1:
        for x in range(x1,x1 + h1):
            if x == x2:
                for y in range(y1,y1 + w1):
                    if y == y2:
                        return True
    return False