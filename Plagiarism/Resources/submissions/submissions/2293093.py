def lucky_numbers(n):
    last_seq = []
    k = 1
    for i in range(1, n+1):
        last_seq.append(i)
    new_seq = last_seq[:]
    while k <= len(new_seq):
        new_seq = last_seq[:]
        for m in range(0, n):
            if last_seq[m] % k == 0:
                new_seq[m:m] = []
        k += 1
        last_seq = new_seq[:]
    return last_seq