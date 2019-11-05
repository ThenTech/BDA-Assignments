types = "ACGT"


def print_dna(n, output):
    if len(output) == n:
        print(output)
    else:
        for i in types:
            print_dna(n, output + i)


print_dna(int(input("n = ?\n")), "")
