def f_dna(first, dna, n):
    if (n == 0):
        print(first)
    else:
        for i in range(len(dna)):
            new_first = first + dna[i]
            f_dna(new_first, dna, n-1)

def dna_helper(n):
    dna = "ACGT"
    for i in range(len(dna)):
        first = dna[i]
        f_dna(first, dna, n-1)



dna_helper(int(input()))