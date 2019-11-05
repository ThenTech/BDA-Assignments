dna = ["A", "G", "T", "C"]
def hoi(n):

    newlist = []
    if n == 1:
        return dna
    for i in range(4):
        for j in hoi(n-1):
            newlist.append(dna[i] + j)
    for h in newlist:
        print(h)
n = int(input())
if n == 1:
    for k in dna:
        print (k)
hoi(n)