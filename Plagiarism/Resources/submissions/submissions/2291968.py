def is_ordered(list):
    for x in range(1,len(list)):
        if list[x - 1] > list[x]:
            return False
    return True