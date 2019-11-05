n = 0


def remove_unlucky(sequence, step):
    result = []
    for i in range(len(sequence)):
        if (i+1) % step != 0:
            result.append(sequence[i])

    return result


def lucky_numbers(n):
    sequence = [ i for i in range(1, n + 1)]
    step = 2
    while step < len(sequence):
        sequence = remove_unlucky(sequence, step)
        step += 1
    return sequence
    

print(lucky_numbers(n))
