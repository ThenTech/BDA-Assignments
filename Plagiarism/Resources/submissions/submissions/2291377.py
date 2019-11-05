def is_ordered(l):
    x = l[:]
    x.sort()
    
    if x == l:
        return True
    else:
        return False

is_ordered([1, -2, 3, 4])
