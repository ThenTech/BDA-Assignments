def does_line_intersect(p1, l1, p2, l2):
    start = max(p1, p2)
    end = min(p1+l1, p2+l2)
    return start < end


def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    return does_line_intersect(x1, w1, x2, w2) and \
                    does_line_intersect(y1, h1, y2, h2)
