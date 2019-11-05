def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    countx = 0
    county = 0
    for i in range(h1):
        y = y1 + i
        for j in range(h2):
            y5 = y2 + j
            if y == y5:
                countx = 1

    for i in range(w1):
        x = x1 + i
        for j in range(w2):
            x5 = x2 + j
            if x == x5:
                county = 1
    return (countx + county) == 2