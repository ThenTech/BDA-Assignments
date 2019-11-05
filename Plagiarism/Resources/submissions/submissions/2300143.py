def lucky_numbers(a):
    step = 2
    while len(a) > step:
        filtered_list = [a[i - 1] for i in range(len(a) + 1) if i % step != 0]
        step += 1
        a = filtered_list
    return a
