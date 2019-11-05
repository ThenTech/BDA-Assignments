def shift(l, n):
    newlist = l[:]
    
    for values in range(len(l)):
        position = values
        while values + n >= len(l):
            values = values - len(l) + 1
        while values + n < 0:
            values = values + len(l) - 1
        newlist[values] = l[position]
    return newlist
            