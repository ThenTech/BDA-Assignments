def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    for i in range(x1,w1+1):
        if i == y2 or i == y2+w2:
            for k in range(y2,y2+h2+1):
                if k == x1 or k == x1+w1:
                    return True
    return False