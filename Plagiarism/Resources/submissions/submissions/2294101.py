def is_ordered(l):
    ordered = True 
    for index in range(len(l)):
        if index == len(l) - 1:
            return True
        elif l[index] <= l[index + 1]:
            ordered = ordered and True
        else:
            return False
    return ordered