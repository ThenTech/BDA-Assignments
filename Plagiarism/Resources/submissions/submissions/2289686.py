def is_ordered(l):
    difference = l[1] - l[0]
    for i in range(2:len(l)):
        if l[i-1] - difference != l[i]:
            return False
    return True
    pass