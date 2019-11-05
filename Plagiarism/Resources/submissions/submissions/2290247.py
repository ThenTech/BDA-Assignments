def is_ordered(l):
    for i in range(len(l)):
        if l[i]>l[i+1]:
            return False
    return True