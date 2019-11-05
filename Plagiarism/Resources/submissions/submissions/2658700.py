def lucky_numbers(n):
    new_list = []
    for i in range(1, n):
        new_list.append(i)

    x = 2
    while x <= len(new_list):
        help_list = []
        for i in range(len(new_list)):
            if (i + 1) % x != 0:
                help_list.append(new_list[i])

        new_list = help_list
        x += 1

    return new_list
        