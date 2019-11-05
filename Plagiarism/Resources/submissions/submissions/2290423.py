def is_ordered(list):
    mylist = list[:]
    list.sort()
    if mylist == list:
        return True
    else:
        return False

