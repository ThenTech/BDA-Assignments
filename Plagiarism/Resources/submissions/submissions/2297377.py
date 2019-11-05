def is_ordered(l):
    for i in range(l, len(l)):
        if l[i] < l[i-1]:
            return False
    return True
        