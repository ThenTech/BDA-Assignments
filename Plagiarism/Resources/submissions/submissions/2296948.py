def lucky_numbers(n):
    numbers_list = [i for i in range(1, n + 1)]
    bool_list = [True]
    lucky_list = []
    
    for i in range(2, n + 1):
        if numbers_list[i] % i == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    
    for index in range(len(bool_list)):
        if bool_list[index]:
            lucky_list.append(numbers_list[index])
    
    return lucky_list