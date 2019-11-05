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
    if len(input) > 1:
        returnlijst = recurse(input[1:])
        for i in range(len(returnlijst)):
            list.append(input[:len(input)-1] + returnlijst[i])
            list.append("" + returnlijst[i])
            lijst.append(input[:len(input) - 2] + returnlijst[i])
            lijst.append(""+ returnlijst[i])
        return(lijst)


    if len(input) == 1:
        lijst.append(input[0])
        lijst.append("")
        list.append(input[0])
        list.append("")
        return(lijst)

recurse(input2)

for i in list:
    print(i)
