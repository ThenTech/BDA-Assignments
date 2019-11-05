def lucky_numbers(n):
    list = []
    for i in range(1, n):
        list.append(i)
    
    newlist = list[:]
    value = 2
    while value < len(newlist):
        secondval = value
        removed = 0
        while secondval < len(newlist):
            del list[secondval-1- removed]
            secondval += value
            removed += 1
        value += 1
        newlist = list[:]
    return newlist