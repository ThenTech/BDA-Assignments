def lucky_numbers(n):
    numbers_list = [i for i in range(1, n + 1)]
    bool_list = []
    lucky_list = []
    
    for i in range(2, n):
        if numbers_list[i] % i == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    
    for index, element in enumerate(numbers_list):
        if bool_list[index]:
            luck_list.append(numbers_list[index])
    
    return lucky_list
        