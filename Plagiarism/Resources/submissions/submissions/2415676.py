def print_helper(length, alphabet, prefix):
    if len(prefix) == length:
        print(prefix)
    else:
        for char in alphabet:
            print_helper(length, alphabet, prefix+char)

def print_dna(length):
    bases = "ACGT"
    print_helper(length, bases, "")
    
length = int(input())