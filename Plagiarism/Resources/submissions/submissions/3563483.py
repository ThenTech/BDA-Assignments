def is_unique(l):

    test = True
    numbers = []

    for i in range(len(l)):

        if l[i] in numbers:                       
            return False
        numbers += [l[i]]                           

    return test