def lucky_numbers(n):
    l = []
    for i in range(1, n + 1):
        l.append(i)
    return l

def removeUnlucky(list, g):
    i = 0
    if g > len(list):
        print(list)
        return
    else:
        while (i + g) < len(list):
            i += g
            list.remove(list[i])
        return list


def preset(n):
    g = 1
    listlucky = lucky_numbers(n)
    while g < len(listlucky):
        removeUnlucky(listlucky, g)
        g += 1
    print(listlucky)