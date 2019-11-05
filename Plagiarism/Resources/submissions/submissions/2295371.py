def is_ordered(l):
    list = l[:]
    new_list = list.sort()
    if new_list == list:
        print(True)
    else:
        print(False)
    
    