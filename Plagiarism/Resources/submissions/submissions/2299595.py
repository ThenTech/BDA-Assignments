def is_ordered(l):
    copy = l[:]
    copy.sort()
    if copy == l:
        return True
    else:
        return False

is_ordered([1, 2, 3, 4, 5, 6, 7, 8, 9])