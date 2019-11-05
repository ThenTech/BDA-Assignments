def is_ordered(l):
    ordered_list = l.sort()
    if l == ordered_list or l == [] or l == l.sort(reverse = True):
        return True
    else:
        return False