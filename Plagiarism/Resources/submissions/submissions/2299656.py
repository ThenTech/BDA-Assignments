def absolutewaarde(x):
    teller = 0
    while x < 0:
        x += 1
        teller += 1
    return teller


def groter_als_nul(l, n):
    new_list = []

    while n > 0:
        new_list.append(l[len(l) - n])
        del l[len(l) - n]
        n -= 1
    new_list.extend(l)
    return new_list


def kleiner_als_nul(l, n):
    copy_list = l[:]
    new_list = []
    teller = 0
    n = absolutewaarde(n)
    for i in range(n):
        new_list.append(copy_list[teller])
        del l[teller]
        teller += 1
    l.extend(new_list)
    return l

def shift(l, n):
    if n < 0:
        return kleiner_als_nul(l, n)
    elif n > 0:
        return groter_als_nul(l, n)
    else:
        return l
