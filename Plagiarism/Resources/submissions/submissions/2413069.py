dna = 'ACGT'
count = int(input('Count: '))
n = len(dna) ** count


def print_possibilities(n):
    for x in range(n):
        for i in range(count - 1, -1, -1):
            print(dna[int(x / 4 ** i) % len(dna)], end="")
        print()


print_possibilities(n)