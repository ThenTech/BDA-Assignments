def is_ordered(list):
    sorted = list[:]
    sorted.sort()
    if sorted == list:
        print(True)
    else:
        print(False)