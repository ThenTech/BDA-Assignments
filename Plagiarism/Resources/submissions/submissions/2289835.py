def is_ordered(l):
    for i in range(len(l)):
        if l[i] < l[i+1] and l[i] != len(l):
            continue
        elif l[i] == len(l):
            return True
        else:
            return False
    return True