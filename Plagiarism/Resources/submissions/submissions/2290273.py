def is_ordered(l):
    ordered_list = l.sort()
    if l == ordered_list:
        return True
    else:
        return False