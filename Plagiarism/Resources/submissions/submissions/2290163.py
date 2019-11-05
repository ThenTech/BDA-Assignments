def is_ordered(list):
    sorted = list[:]
    sorted.sort()
    if sorted == list:
        return True
    else:
        return False