def is_ordered(l):

    test = False
    for i in range(1,len(l)):
        if i >= l[i - 1]:
            test = True
        else:
            return False
    return test
