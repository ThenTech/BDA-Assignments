def dna(dna, n):
    for i in dna:
        dna_helper(dna, i, n)
        

def dna_helper(dna, first, n):
    if len(first) == n:
        print(first)
    else:
        for i in dna:
            end = i
            output = first + end
            dna_helper(dna, output, n)

n = int(input("n?"))
dna("ACGT", n)