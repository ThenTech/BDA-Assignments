def is_unique(l):
    u = True
    for i in range(len(l) - 1):
        counter = i
        while counter < len(l) - 1:
            if l[counter] == l[counter + 1]:
                u = False
                break
            else:
                counter += 1

    if u:
        return True
    else:
        return False