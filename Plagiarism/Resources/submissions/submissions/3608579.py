def lucky_numbers(n):
    if n == 0:
        return []
    place = 2
    list = []

    for i in range(1, n + 1):
        list.append(i)

    while place < len(list):
        buffer = list[:]
        for i in range(1, len(buffer)):
            if i % place == 0:
                list.remove(buffer[i-1])
        place += 1
    return list