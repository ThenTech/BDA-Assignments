def is_unique(list):
    for x in range(len(list)):
        for y in range(x + 1,len(list)):
            if list[x] == list[y]:
                return False
    return True