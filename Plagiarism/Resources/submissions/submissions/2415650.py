def print_helper(n, alphabet, prefix):
    if len(prefix) == n:
        print(prefix)
    else:
        for char in alphabet:
            print_helper(n, alphabet, prefix+char)

def print_dna(n):
    bases = "ACGT"
    print_helper(n, bases, "")