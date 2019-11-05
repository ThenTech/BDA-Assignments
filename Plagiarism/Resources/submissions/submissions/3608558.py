def lucky_numbers(n):
    if n == 0:
        return []
    place = 2
    list = []
    
    for i in range(n):
        list.append(i)
    
    while place < len(list):
        for i in range(len(list)):
            if i % place == 0:
                del list[i]
        place += 1
    return list