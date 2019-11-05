def is_ordered(l):
    for position in range(len(l)-1):
        if not l[position] <= l[position+1]:
            return False
    return True
    
    