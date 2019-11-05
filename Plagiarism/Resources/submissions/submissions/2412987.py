dna = 'ACGT'
count = int(input('Count: '))
n = (len(dna) ** count) - 1


def print_possibilities(n):
    if n == -1:
        return
    print_possibilities(n-1)
    for i in range(count-1, -1, -1):
        print(dna[int(n/4 ** i) % len(dna)], end="")
    print()


print_possibilities(n)