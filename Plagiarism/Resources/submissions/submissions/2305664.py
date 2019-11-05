def lucky_numbers(n):
    sequence = [ i for i in range(1, n + 1)]
    step = 2
    while (step < len(sequence)):
        sequence = [ sequence[i]
                     for i in range(len(sequence))
                     if i % step != step - 1]
        step += 1
    return sequence


n = int(input("Give n: "))
print(lucky_numbers(n))
