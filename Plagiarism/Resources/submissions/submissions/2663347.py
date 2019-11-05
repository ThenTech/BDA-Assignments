def possible_combinations(dna, prefix, n):
    for char in dna:
        if len(prefix + char) == n:
            print(prefix + char)
        else:
            possible_combinations(dna, prefix + char, n)

dna = 'ACGT'
n = int(input(': '))
possible_combinations(dna, "", n)