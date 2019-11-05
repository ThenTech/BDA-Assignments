def lucky_numbers(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
     #list created
    copy = list[:]
    for j in range(1, n):
        if j > len(copy):
            return copy
        for x in range(1, 10):
            y = j*x
            if y > len(copy):
                break


            del copy[y]





    return copy
lucky_numbers(22)
