def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if x2 or x2+w2 in range(x1, x1+w1+1):
        if y2 or y2+h2 in range(y1, y1+h1+1):
            return True
        else:
            return False
    else:
        return False