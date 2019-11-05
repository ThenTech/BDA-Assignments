# write your code here
def dna(n):
    recursie(n,"")
def recursie(n,totaal):
    if n ==0:
        print(totaal)
    else:
        for i in "ACGT":
            dna(n-1,totaal+i)
n=int(input())
dna(n)