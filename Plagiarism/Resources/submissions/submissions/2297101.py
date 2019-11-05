def shift(list, n):
    n *= -1
    list2 = [list[x + n] for x in range(len(list)) if x + n + 1< len(list)]
    if n >0:
        list2.append(list[len(list) - 1])
        for x in range(len(list)-len(list2)):
            list2.append(list[x])
    return list2