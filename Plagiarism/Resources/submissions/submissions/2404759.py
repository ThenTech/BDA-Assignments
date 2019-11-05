list = ["A", "C", "G", "T"]
list_2 = []
copy = list[:]
counter = 0
def dna(n):
    global counter
    global copy
    global list
    global list_2
    counter = 0
    if len(list) == 0:
        return list_2
    else:
        for i in range(4):
            combo = copy[counter] + copy[i]
            print(combo)
            counter += 1
        del list[0]
    dna(n)

dna(2)