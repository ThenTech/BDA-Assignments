def print_help(lengte, alfabet, prefix):
    if len(prefix) == lengte:
        print(prefix)
    else:
        for i in alfabet:
            prefix += i
            print_help(lengte, alfabet, prefix)


def dna(length):
    bases = "ACGT"
    print_help(length, bases, "")
    
dna(int(input()))