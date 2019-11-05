def is_ordered(list):
    sorted_list = list.sort()
    if sorted_list == list:
        return True
    else:
        return False
