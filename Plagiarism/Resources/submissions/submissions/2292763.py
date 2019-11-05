def is_ordered(l):
    copy = l[:]
    sorted_copy = copy.sort()
    
    for i in range(copy):
        return copy[i] == sorted_copy[i]