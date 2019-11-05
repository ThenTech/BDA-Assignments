def is_ordered(l):
    last = l[0]
    for x in l:
        if x >= last:
            continue
        else:
            return False
    return True