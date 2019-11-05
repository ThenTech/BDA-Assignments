def is_ordered(l):
    copy = l[:]
    sorted_copy = copy.sort()

    if copy == sorted_copy:
        return True