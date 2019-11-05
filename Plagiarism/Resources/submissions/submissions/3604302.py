def f_dna(n, total, dna):
    if(len(total) == n):
        print(total)
    else:
        for letter in dna:
            new_total = total+ letter
            f_dna(n, new_total, dna)



def f_dna_helper(n):
    f_dna(n, "" ,"ACGT")


f_dna_helper(int(input()))