def lucky_numbers(n):
    lucky_list = list(range(1, n))
    count = 2
    while len(lucky_list) > count:
        lucky_list_edit = [lucky_list[index-1] for index in range(1, len(lucky_list)+1) if index % count != 0]
        lucky_list = lucky_list_edit
        count += 1
    return lucky_list
