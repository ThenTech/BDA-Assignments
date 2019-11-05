def shift(l, n):
    newlist = l[:]
    
    for values in range(len(l)):
        position = values
        values = values + n
        while values >= len(l):
            values = values - len(l)
        while values < 0:
            values = values + len(l) 
        newlist[values] = l[position]
    return newlist