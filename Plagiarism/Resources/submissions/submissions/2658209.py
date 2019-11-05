def is_ordered(l):
    x = True
    for i in range(len(l)):
        if i + 1 <= len(l)-1 and l[i] > [i + 1]:
            x = False
    return x
        