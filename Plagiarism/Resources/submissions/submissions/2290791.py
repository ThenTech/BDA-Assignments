def is_ordered(l):
    last = l[0]
    for i in range(1, len(l)-1):
        if l[i] < last:
            return False
        last = l[i]
    return True
