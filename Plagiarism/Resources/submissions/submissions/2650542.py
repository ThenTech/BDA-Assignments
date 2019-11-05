def generate_sequence(n):
    l = []
    for i in range(1, n + 1):
        l.append(i)
    return l


def lucky_numbers(n):
    l = generate_sequence(n)
    new_l = []
    element = 2

    while element <= len(l):
        for i in range(1, len(l) + 1):
            if i % element != 0:
                new_l.append(l[i - 1])

        l = new_l
        new_l = []
        element += 1

    return l