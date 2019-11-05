def is_ordered(l):
    for i in l:
        if int(l[i]) > int(l[i+1]):
            return False

    return True


is_ordered([1, 3, 2, 4])
