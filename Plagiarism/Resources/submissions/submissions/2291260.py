def is_unique(list):
    copy = list[:]
    for item in list:
        counter = 0
        for copiedItem in copy:
            if item == copiedItem:
                counter+= 1

        if counter > 1:
            return False
    return True