def remover(lijst,i):
    nieuwe_lijst = []
    for j in range(len(lijst)):
        if (j+1) % i != 0:
            nieuwe_lijst.append(lijst[j])
    return nieuwe_lijst


def lucky_numbers(n):
    seq = [i for i in range(1, n + 1)]
    i = 2
    while i <= len(seq):
        lijst = remover(seq,i)
        seq = lijst
        i = i + 1
    return seq