def lucky_numbers(n):
    list = [x for x in range(1, n+1)]
    list_temp = []
    for i in range(2, n+1):
        for spot in range(len(list)):
            if (spot+1) % i != 0:
                list_temp.append(list[spot])
        list = list_temp
        list_temp = []

    return list