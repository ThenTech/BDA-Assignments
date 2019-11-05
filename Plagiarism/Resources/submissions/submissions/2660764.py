def print_helper(length, combs, prefix):
    if len(prefix) == length:
        print(prefix)
    else:
        for char in combs:
            print_helper(length, combs, prefix + char)


def print_dna(length):
    combs = "ACGT"
    print_helper(length, combs, "")