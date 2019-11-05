def lucky_numbers(number):
    new_list = [i for i in range(1, number+1)]

    count = 2
    while count <= len(new_list):
        helper = []
        for i in range(0, len(new_list[:])):
            if (i+1) % count != 0:
                helper.append(new_list[i])
        new_list = helper
        count += 1
    return new_list
