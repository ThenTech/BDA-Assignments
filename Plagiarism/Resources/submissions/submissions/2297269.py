def lucky_numbers(n):
    last_seq = []
    k = 2
    count = 0
    for i in range(1, n+1):
        last_seq.append(i)
    new_seq = last_seq[:]
    while k <= len(last_seq):
        new_seq = last_seq[:]
        for m in range(0, len(last_seq)):
            if last_seq[m] % k == 0:
                del new_seq[m - count]
                count += 1
        k += 1
        last_seq = new_seq[:]
    return last_seq