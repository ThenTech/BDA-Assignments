def DNA(n):
    dna=[]
    if n !=0:
        for i in "ACGT":
            for j in DNA(n-1):
                a=j+i
                dna.append(a)
    else:
        return " "
    return dna


for i in DNA(n):
    print(i[1:])