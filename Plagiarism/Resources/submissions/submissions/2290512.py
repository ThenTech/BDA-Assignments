def is_ordered(l):
    ordered_list = l.sort()
    if l == ordered_list or l == ordered_list.sort():
        return True
    else:
        return False