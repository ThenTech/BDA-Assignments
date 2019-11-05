def is_unique(l):
    standard = l
    i = 0
    while i < len(l):
        l = standard
        adapted_l = l.remove(l[i])
        if l[i] in adapted_l:
            return False
        i += 1
    return True