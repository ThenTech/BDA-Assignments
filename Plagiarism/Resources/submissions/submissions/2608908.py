def is_ordered(l):
    for index in range(len(l)-1):
        if l[index] > l[index+1]:
            return False
    return True