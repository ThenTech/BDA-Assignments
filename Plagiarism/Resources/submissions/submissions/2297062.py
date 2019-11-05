def lucky_numbers(n):
    l1 = [i for i in range(1, n+1)]
    for i in range(2, len(l1)):
        del l1[i-1::i]
    return l1