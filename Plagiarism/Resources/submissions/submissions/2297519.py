def lucky_numbers(n):
    list = [x+1 for x in range(n)]
    x = 1
    while x < len(list):
        y = 0
        while y in range(len(list)):
            if y % x == 0:
                list.remove(list[y])
            y+=1
        x+=1
    return list