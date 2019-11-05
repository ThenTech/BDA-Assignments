def lucky_numbers(n):
    if n == 0:
        return []
    place = 2
    list = []
    
    for i in range(n):
        list.append(i)
    
    while place < len(list):
        buffer = list[:]
        for i in range(len(buffer)):
            if i % place == 0:
                list.remove(buffer[i])
        place += 1
    return list