def lucky_numbers(n):
    listy = []
    for i in range(1, n + 1):
        listy.append(i)

    listy_copy = listy[:]
    j = 2
    while j < len(listy_copy):
        for x in listy_copy:
            if x % j == 0:
                listy.remove(x)
            listy_copy = listy
        j += 1
    return listy_copy