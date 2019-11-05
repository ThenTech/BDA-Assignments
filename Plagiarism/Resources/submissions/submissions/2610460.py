def recursion_dna2(length, list_dna, prefix):
    if len(prefix) == length:
        print(prefix)
    else:
        for i in list_dna:
            recursion_dna2(length, list_dna, prefix + i)

def recursion_dna(length):
    list_dna = ["A", "C", "G", "T"]
    recursion_dna2(length, list_dna, "")