list = []


def recursion(first, second):
    last = len(first) == 1
    n = len(first[0])
    for i in range(n):
        item = second + first[0][i]
        if last:
            list.append(item)
        else:
            recursion(first[1:], item)


dna = [["A", "C", "G", "T"], ["A", "C", "G", "T"]]
recursion(dna, "")
for i in list:
    print(i)