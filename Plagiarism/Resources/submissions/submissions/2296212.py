def lucky_numbers(n):
    list = []
    j = 2

    for i in range(1, n + 1):
        list = list + [i]
    list_copy = list[:]

    while j <= len(list):
        for i in range(0, len(list)):
            if (i + 1) % j == 0:
                number = list_copy[i]
                list.remove(number)
        list_copy = list[:]
        j = j + 1
    return list