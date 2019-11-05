def lucky_numbers(n):
    newlist = n[:]
    value = 2
    while value < len(newlist):
        secondval = 0
        while secondval < len(newlist):
            secondval += value
            n.remove(newlist[secondval])
        value += 1
        newlist = n[:]
        