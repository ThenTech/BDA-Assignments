def is_ordered(l):
    if len(l) > 0:
        last = l[0]
        for x in l:
            if x >= last:
                continue
            elif x < last:
                return False
        return True
    else:
        return True