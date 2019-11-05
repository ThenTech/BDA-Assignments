def lucky_numbers(n):
    newlist = n[:]
    value = 2
    while value < len(newlist):
        secondval = 0
        while secondval < len(newlist):
            secondval += value
            del n[secondval]
        value += 1
        newlist = n[:]
        