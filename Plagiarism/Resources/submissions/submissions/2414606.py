def print_helper(length, alphabet, prefix):
    if len(prefix) == length:
        print(prfix)
    else:
        for char in alphabet:
            print_helper(length, alphabet, prefix + char)
            

def print_dna(length):
    bases = "ACGI"
    print_helper(length, bases, "")
    
print_dna(int(length))