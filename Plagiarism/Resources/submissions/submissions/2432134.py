list = []
input = int(input("Input: "))


def recursion(first, second):
    last = len(first) == 1
    n = len(first[0])
    for i in range(n):
        item = second + first[0][i]
        if last:
            list.append(item)
        else:
            recursion(first[1:], item)


dna = input*('ACGT',)
recursion(dna, "")
for j in list:
    print(j)
