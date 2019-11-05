def lucky_numbers(n):
    list = [x+1 for x in range(n)]
    x = 1
    while x < len(list):
        list2 = list[:]
        for y in list2:
            if y % x == 0:
                print(y)
                list.remove(list[y])
        print(list)
        x+=1
    return list