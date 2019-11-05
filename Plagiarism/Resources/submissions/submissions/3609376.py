def f_dna_helper(first, dna, n):
    if (n == 0):
        print(first)
    else:
        for i in dna:
            new_first = first+ i
            f_dna_helper(new_first, dna, n-1)

def f_dna(n):
    dna = "ACGT"
    f_dna_helper("", dna, n)


f_dna(int(input()))