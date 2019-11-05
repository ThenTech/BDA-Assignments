def is_ordered(l):
    for i in len(l)-1:
        if l[i-1] < l[i]:
        else:
            return False
    return True