def get_dna(lenght, bases, prefix):
    if len(prefix) == lenght:
        print(prefix)
        return prefix
    else:
        for char in bases:
            get_dna(lenght, bases, prefix + char)
            
def dna(n):
    bases = "ACGT"
    get_dna(n, bases, "")

input(dna(n))