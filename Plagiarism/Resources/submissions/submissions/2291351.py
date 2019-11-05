def lucky_numbers(n):
    list = []
    for i in range(1, n)
        list.append(n)
    
    newlist = list[:]
    value = 2
    while value < len(newlist):
        secondval = 0
        while secondval < len(newlist):
            secondval += value
            del list[secondval]
        value += 1
        newlist = list[:]
        