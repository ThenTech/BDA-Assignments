def is_ordered(l):
    list = l[:]
    ordered_list = l.sort()
    if l == ordered_list or l == []:
        return True
    else:
        return False