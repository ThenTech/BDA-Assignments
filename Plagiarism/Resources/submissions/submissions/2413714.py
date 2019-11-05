def hoi(n):
    dna = ["A", "G", "T", "C"]
    newlist = []
    if n == 1:
        return dna
    for i in range(4):
        for j in hoi(n-1):
            newlist.append(dna[i] + j)
    return newlist
n = int(input())
print(hoi(n))