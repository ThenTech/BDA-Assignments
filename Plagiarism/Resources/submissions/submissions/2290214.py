def is_ordered(l):
    sorted_list = l[:]
    sorted_list.sort()
    return l == sorted_list