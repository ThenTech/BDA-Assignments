def printer(lenght, dna, prefix):
    if lenght == len(prefix):
        print(prefix)
    else:
        for char in "ACGT":
            printer(lenght, dna, prefix + char)


def bases(lenght):
    dna = "ACGT"
    printer(lenght, dna, "")

bases(int(input("input?")))