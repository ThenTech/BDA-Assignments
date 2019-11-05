def is_ordered(l):
    ordered = True
    for i in range(0, len(l) - 1):
        if l[i] < l[i+1]:
            continue
        else:
            ordered = False
            break
    return ordered

