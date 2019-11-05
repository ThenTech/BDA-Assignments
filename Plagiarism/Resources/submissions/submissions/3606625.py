def f_dna_helper(first, dna, n, li):
    if (n == 0):
        return [first]
    else:
        for i in dna:
            new_first = first+ i
            li += f_dna_helper(new_first, dna, n-1, li)
        return li

def f_dna(n):
    dna = "ACGT"
    for i in dna:
        first = i
        li = f_dna_helper(first, dna, n-1, [])
        for el in li:
            print(el)

f_dna(int(input()))