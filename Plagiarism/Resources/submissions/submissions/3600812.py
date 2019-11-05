def lucky_numbers(n):
    list = []
    for i in range(1, n+1):
        list.append(i)
    i = 2
    while i < len(list):
        n_list = []
        n_list.append(list[0])
        for elem in range(1, len(list)):
            if elem % i != 0:
                n_list.append(list[elem-1])
        list = n_list
        i += 1
    return list