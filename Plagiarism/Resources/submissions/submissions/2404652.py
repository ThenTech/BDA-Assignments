dna = ["A", "C", "G", "T"]
count = 0
x = 0
number = int(input(":  "))


def combinations(n):
    global dna, count, number, x
    if count == number ** len(dna):
        return
    if n == len(dna):
        n = 0
        x += 1
    print(dna[x], dna[n], sep="")
    count += 1
    combinations(n + 1)


combinations(0)
