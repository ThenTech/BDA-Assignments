def is_ordered(l):

    test = False
    if len(l) == 1 or len(l) == 0:
        return True

    for i in range(1,len(l)):
        if l[i] >= l[i - 1]:
            test = True
        else:
            return False

    return test
