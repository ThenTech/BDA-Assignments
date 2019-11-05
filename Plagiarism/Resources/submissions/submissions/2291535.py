def is_ordered(list):
    count = 0
    for number in list[1:]:
        if number >= list[count]:
            count = count + 1
        else:
            return False
    return True