def in_between(x_left1, x_right1, center):
    if center > x_left1 and center < x_right1:
        return True
    else:
        return False

def does_intersect(x_left1, y_down1, w1, h1, x_left2, y_down2, w2, h2):
    x_right1 = x_left1 + w1
    x_right2 = x_left2 + w2
    y_up1 = y_down1 + h1
    y_up2 = y_down2 + h2
    x1 = in_between(x_left1, x_right1, x_left2)
    x2 = in_between(x_left1, x_right1, x_right2)
    y1 = in_between(y_down1, y_up1, y_down2)
    y2 = in_between(y_down1, y_up1, y_up2)
    if (x1 == True or x2 == True) and (y1 == True or y2 == True):
        return True
    else:
        return False
