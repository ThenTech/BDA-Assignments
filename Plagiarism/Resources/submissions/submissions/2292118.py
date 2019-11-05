def fibonacci_values(i):
    list = [0, 1]
    if i == 0:
        list = list[0:1]
        print(list)
    elif i == 1:
        list = list[1:2]
        print(list)
    else:
        for x in range(2, i):
            number = list[x-1] + list[x-2]
            list.append(number)
        print(list)