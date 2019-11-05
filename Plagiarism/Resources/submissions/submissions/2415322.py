# write your code here
def dna(n):
    vorige = ""
    helper(n,vorige)

def helper(n,vorige):
    if n == 0:
        return ""
    else:
        for base in "ACGT":
            vorige += base
            print(base + helper(n-1,vorige))
dna(2)