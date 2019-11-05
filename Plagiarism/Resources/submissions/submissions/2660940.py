def is_ordered(listy):
    for i in range(len(listy)-1):
        if listy[i] < listy[i+1]:
            continue
        else:
            return False
    return True