n=int(input("give a number"))
def DNA(n):
    bases=[]
    if n == 0:
        return [""]
    else:
        for i in "ACGT":
            for j in DNA(n-1):
                base = j + i
                bases.append(base)
    return bases




for i in DNA(n):
    print(i)