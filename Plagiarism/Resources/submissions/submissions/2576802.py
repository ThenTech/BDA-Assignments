def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    width1 = range(x1, x1+w1)
    height1 = range(y1, y1+h1)
    width2 = range(x2, x2+w2)
    height2 = range(y2, y2+h2)

    for i in width1:
        if i in width2:
            for j in height1:
                if j in height2:
                    if i != x2 and i != x2+w2 and j != y2 and j != y2+h2:
                        return False
                    else:
                        return True
            return False 
    return False