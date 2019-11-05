def dna(string, n):
    if n == 0:
        print(string)
        return
    dna(string + 'A', n-1)
    dna(string + 'C', n - 1)
    dna(string + 'T', n - 1)
    dna(string + 'G', n - 1)


dna('', int(input()))
