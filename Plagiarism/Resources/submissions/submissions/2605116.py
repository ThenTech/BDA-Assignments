def lucky_numbers(number):
    list_numbers = []
    for i in range(1,number+1):
        list_numbers.append(i)

    step = 2
    while len(list_numbers) >= step:
        new_list = []
        for i in range(len(list_numbers)):
            if (i+1) % step != 0:
                new_list.append(list_numbers[i])
        list_numbers = new_list
        step += 1
    return list_numbers

print(lucky_numbers(22))