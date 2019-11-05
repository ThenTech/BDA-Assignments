def print_help(length, alfabet, prefix):
    if len(prefix) == length:
        print(prefix)
    else:
        for i in alfabet:
            prefix += i
            print_help(length, alfabet, prefix)


def dna(length):
    bases = "ACGT"
    print_help(length, bases, "")
    
dna(int(input()))