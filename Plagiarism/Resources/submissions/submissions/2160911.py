def does_intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    left_1 = ""
    for i in range(y1, y1 + h1):
        left_1 = left_1 + str(x1) + str(i) + " "
    right_1 = ""
    for i in range(y1, y1 + h1):
        right_1 = right_1 + str(x1 + w1) + str(i) + " "
    top_1 = ""
    for i in range(x1, x1 + w1):
        top_1 = top_1 + str(i) + str(y1 + h1) + " "
    bottom_1 = ""
    for i in range(x1, x1 + w1):
        bottom_1 = bottom_1 + str(i) + str(y1) + " "

    left_2 = ""
    for i in range(y2, y2 + h2):
        left_2 = left_2 + str(x2) + str(i) + " "
    right_2 = ""
    for i in range(y2, y2 + h2):
        right_2 = right_2 + str(x2 + w2) + str(i) + " "
    top_2 = ""
    for i in range(x2, x2 + w2):
        top_2 = top_2 + str(i) + str(y2 + h2) + " "
    bottom_2 = ""
    for i in range(x2, x2 + w2):
        bottom_2 = bottom_2 + str(i) + str(y2) + " "

    if top_1 == bottom_2:
        return False
    elif top_2 == bottom_1:
        return False
    elif right_1 == left_2:
        return False
    elif right_2 == left_1:
        return False
    elif left_2 in top_1 or bottom_1:
        return True
    elif right_2 in top_1 or bottom_1:
        return True
    elif left_1 in top_2 or bottom_2:
        return True
    elif right_1 in top_2 or bottom_2:
        return True