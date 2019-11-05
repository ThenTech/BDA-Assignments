def is_ordered(list):
    sortedList = list[:]
    sortedList.sort()
    for index in range(0, len(list)):
        if sortedList[index] != list[index]:
            return False
    return True