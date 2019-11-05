def is_ordered(list):
    orde = True
    for i in range(len(list) - 1):
        if i == 0:
            if list[i] > list[i + 1]:
                orde = False
        else: 
            if list[i] > list[i + 1]:
                orde = False
    return orde
    