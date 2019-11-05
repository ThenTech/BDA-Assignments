def is_ordered(l):
    for i in range(1, len(l)-1):
        if l[i] < l[i-1]:
            return False
    return True
