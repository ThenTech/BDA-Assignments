def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 <= x2 and y1 <= y2 and y1+h2 <= y2:
        return False
    elif x1 >= x2 and y1 >= y2 and y1+h2 >= y2:
        return False
    elif x1 >= x2 and y1 <= y2 and y1+h2 <= y2:
        return False
    elif x1 <= x2 and y1 >= y2 and y1+h2 >= y2:
        return False
    return True