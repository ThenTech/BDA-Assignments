def is_ordered(l):
    for i in range(len(l)):
        if i != len(l)-1 and l[i] <= l[i+1]:
            continue
        elif i == len(l)-1:
            continue
        else:
            return False
    return True