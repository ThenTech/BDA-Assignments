def lucky_numbers(n):
    seq = []
    for i in range(1, n+1):
        seq.append(i)

    curr = 2
    while len(seq) >= curr:
        seq2 = []
        for i in range(1, len(seq)+1):
            if i % curr != 0:
                seq2.append(seq[i-1])
        seq = seq2[:]
        curr += 1

    return seq
