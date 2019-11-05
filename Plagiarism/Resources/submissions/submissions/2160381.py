def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    return bool(x1 + w1 < x2 or x2 + w2 < w1 or y1 + h1 < y2 or y2 + h2 < y1)


print(does_intersect(1,1,2,2,1,3,2,2))