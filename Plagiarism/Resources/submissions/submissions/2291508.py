def lucky_numbers(n):
    list = []
    for i in range(1, n):
        list.append(i)
    
    newlist = list[:]
    value = 2
    while value < len(newlist)-1:
        secondval = value
        while secondval < len(newlist)-1:
            del list[secondval-1]
            secondval += value
        value += 1
        newlist = list[:]
        