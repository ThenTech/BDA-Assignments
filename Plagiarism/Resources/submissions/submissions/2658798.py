def dna_helper(n, first, second, dna):
    if n == 0:
        print(first)
    else:
        for i in dna:
            second = i
            dna_helper(n-1, first+second, "", dna)



def dna(n):
    for i in "ACGT":
        first = i
        dna_helper(n-1, first, "", "ACGT")
        
x = int(input("x"))
dna(x)