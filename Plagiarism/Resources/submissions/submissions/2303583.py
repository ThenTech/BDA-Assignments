def lucky_numbers(n):
    i = 2
    l = [x for x in range(1, n + 1)]
    length = len(l)
    count = 1

    while i < length:
        del l[count::i]
        i += 1
        count += 1
        length = len(l)

    return l