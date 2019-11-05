def shift(list, n):
    if len(list) != 0:
        n *= -1
        n = n % len(list)
        list2 = [list[x + n] for x in range(len(list)) if x + n + 1< len(list)]
        list2.append(list[len(list) - 1])
        if n >0:
            for x in range(len(list)-len(list2)):
                list2.append(list[x])
        return list2
    else:
        return list