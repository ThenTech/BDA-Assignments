def is_ordered(l):
    for i in range(len(l)):
        if i == len(l):
            return True
        elif l[i] > l [i+1]:
            return False
    