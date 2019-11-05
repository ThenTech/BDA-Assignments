def is_unique(l):
    i = 0
    while i < len(l):
        adapted_l = l
        adapted_l[i] = None
        if l[i] in adapted_l:
            return False
        i += 1
    return True