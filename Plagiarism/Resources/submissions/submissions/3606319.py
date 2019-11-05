def lucky_numbers(n):
    list = [i + 1 for i in range(n)]
    copy-list = list[:]
    to_remove = 2
    while to_remove  < len(list):
        k = to_remove
        while k < len(list):
            list.remove(copy_list[k-1])
            k += to_remove
        to_remove += 1
        copy_list = list[:]
    return list
    pass