"""2 cijfers -> 4 verzamelingen
bv. 1 2: [1 2, 1, 2, ]
"""

input = "1 2 3"
input2 = ""
n = 0
list = []

for i in range(len(input)):
    if input[i] != " ":
        input2 += input[i]

def recurse(input):
    lijst = []
    if len(input) > 2:
        returnlijst = recurse(input[1:])
        list.append(input[:len(input)-2] + returnlijst[0])
        list.append(input[:len(input) - 2] + returnlijst[1])
        list.append(input[:len(input) - 2] + returnlijst[2])
        list.append(input[:len(input) - 2] + returnlijst[3])

    if len(input) == 2:
        lijst.append(input[0])
        lijst.append(input[1])
        lijst.append(input)
        lijst.append("")
        list.append(input[0])
        list.append(input[1])
        list.append(input)
        list.append("")
        return(lijst)

recurse(input2)
print(list)
