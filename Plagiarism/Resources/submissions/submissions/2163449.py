def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    x_intersect = as_intersect(x1, w1, x2, w2)
    y_intersect = as_intersect(y1, h1, y2, h2)

    return x_intersect or y_intersect

def as_intersect(coord1, size1, coord2, size2):
    if coord1 < coord2:             #ex: if x1 comes before x2 is x1 + width1 further then x1?
        return coord1+size1 > coord2
    elif coord1 > coord2:                           #ex: if x2 comes before x1 is x2 + width2 further then x1?
        return coord2+size2 < coord1
    return False