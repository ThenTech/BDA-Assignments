def is_unique(list):
    place = 0
    for number in list:
        list_sliced = list[:place] + list[place+1:]
        for figure in list_sliced:
            if number == figure:
                return False
        place = place + 1
    return True