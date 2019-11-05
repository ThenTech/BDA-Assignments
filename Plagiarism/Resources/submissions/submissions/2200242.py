def do_line_fragments_on_same_line_intersect(l1p1, l1p2, l2p1, l2p2):
    return l1p1 < l2p1 < l1p2 or l1p1 < l2p2 < l1p2


def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    rect1_x_axis_projection_point1 = x1
    rect1_x_axis_projection_point2 = x1 + w1
    rect1_y_axis_projection_point1 = y1
    rect1_y_axis_projection_point2 = y1 + h1
    rect2_x_axis_projection_point1 = x2
    rect2_x_axis_projection_point2 = x2 + w2
    rect2_y_axis_projection_point1 = y2
    rect2_y_axis_projection_point2 = y2 + h2
    
    return do_line_fragments_on_same_line_intersect(rect1_x_axis_projection_point1, rect1_x_axis_projection_point2,
        rect1_y_axis_projection_point1, rect1_y_axis_projection_point2)