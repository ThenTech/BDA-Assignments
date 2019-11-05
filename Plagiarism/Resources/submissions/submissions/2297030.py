def lucky_numbers(n):
    numbers_list = [i for i in range(1, n + 1)]
    lucky_list = []
    bool_list = []
    

    count = 0
    while count < len(numbers_list):
        count +=1

        for index, element in enumerate(numbers_list):
            if index % count != 0:
                bool_list.append(True)
            else:
                bool_list.append(False)

        for index, element in enumerate(bool_list):
            if bool_list[index]:
                lucky_list.append(numbers_list[index])

        numbers_list = lucky_list[:]
        lucky_list = []
        bool_list = []

    return numbers_list
