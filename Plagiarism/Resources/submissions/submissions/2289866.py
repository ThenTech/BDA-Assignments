def is_ordered(l):
    for i in range(len(l)):
        if l[i] != len(l) and l[i] < l[i+1]:
            continue
        elif l[i] == len(l):
            return True
        else:
            return False
    return True