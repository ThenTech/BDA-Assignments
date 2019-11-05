dna ='ACGT'

def pos(n):
    hulp("", n)

def hulp(string, n):
    global dna
    if n < 1:
        print(string)
        return
    for x in dna:
        hulp(string+x, n-1)

