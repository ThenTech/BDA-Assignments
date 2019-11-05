def lucky_numbers(n):
    list = [i + 1 for i in range(n)]
    to_remove = 2
    while to_remove  < len(list):
        k = to_remove
        while k < len(list):
            list.pop(k)
            k += to_remove
        to_remove += 1
    return list
    pass