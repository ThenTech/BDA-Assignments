def lucky_numbers(n):
    correct = True
    ln = True
    i = 0
    counter = 2
    l = []
    for h in range(n):
        l.append(h + 1)
    if n == 1:
        return [1]
    while ln == True:
        while correct == True:
            i += counter - 1
            if i >= len(l):
                correct = False
            else:
                del l[i]
        i = 0
        counter += 1
        correct = True

        if counter > len(l):
            ln = False
    return l