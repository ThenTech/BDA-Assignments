def is_ordered(l):
    counter = 0
    ordered = True
    while counter < len(l) - 1:
        if l[counter] < l[counter + 1]:
            counter += 1
        else:
            ordered = False
            break

    if ordered:
        return True
    else:
        return False