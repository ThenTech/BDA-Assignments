def is_ordered(list):
    mylist = list
    sorted_list = mylist.sort()
    if sorted_list == mylist:
        return True
    else:
        return False
