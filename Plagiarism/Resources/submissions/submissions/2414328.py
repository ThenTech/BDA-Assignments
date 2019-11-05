def print_helper(length, alphabet, prefix)
    if (len(prefix) == length):
        print(prefix)
    else:
        for char in alphabet:
            print_helper(length, alphabet, prefix + char)

def print_dna(length):
    bases = "ACTG"
    print_helper(length, bases, "")
    
print_dna(int(input()))
