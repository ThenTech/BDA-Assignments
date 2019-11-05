def lucky_numbers(n):
    list = [i + 1 for i in range(n)]
    to_remove = 2
    while to_remove < len(list):
        k = to_remove
        while k < len(list) - 1:
            list.pop(k-1)
            k += to_remove
        to_remove += 1
    return list
    pass