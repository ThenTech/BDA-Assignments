def lucky_numbers(n):
    numbers_list = [i for i in range(1, n + 1)]
    lucky_list = []

    count = 2
    while count < len(numbers_list):
        count += 1

        for index in enumerate(numbers_list):
            if (index[0] + 1) % count != 0:
                lucky_list.append(index[0] + 1)

        numbers_list = lucky_list[:]
        lucky_list = []

    return numbers_list