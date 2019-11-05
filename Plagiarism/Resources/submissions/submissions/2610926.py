def create_sequence(n):
    list = []
    if n == 1:
        return [1]
    for i in range(1, int(n)):
        list.append(i)
    return list


def lucky_numbers(n):
    sequence = create_sequence(n)
    x = 2
    while x <= len(sequence):
        sequence = remove_numbers(sequence, x)
        x += 1
    return sequence


def remove_numbers(list, n):
    x = 1
    new_list = []
    for i in list:
        if x % n != 0:
            new_list.append(i)
        x += 1
    return new_list