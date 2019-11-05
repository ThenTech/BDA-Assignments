dna = ["A", "C", "G", "T"]


def combinations(n, x, prefix):
    global dna
    if len(prefix + x) == n:
        print(prefix + x)
    else:
        for base in dna:
            combinations(n, base, prefix + x)


number = int(input(":  "))
combinations(number, "", "")
