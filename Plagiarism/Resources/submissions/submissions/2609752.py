def DNA(n):
    global n
    dna=[]
    if n !=0:
        for i in "ACGT":
            for j in DNA(n-1):
                a=j+i
                dna.append(a)
                for i in a:
                    print(i[1:])
    else:
        return " "
    return dna



for i in DNA(n):
    print(i[1:])