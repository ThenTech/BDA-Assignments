"""2 cijfers -> 4 verzamelingen
bv. 1 2: [1 2, 1, 2, ]
"""

input = input('')
input2 = ""
n = 0
list = []
list2 = []

for i in range(len(input)):
    if input[i] != " ":
        input2 += input[i]

def recurse(input):
    lijst = []
    if len(input) > 1:
        returnlijst = recurse(input[1:])
        for i in range(len(returnlijst)):
            list.append(input[:1] + returnlijst[i])
            lijst.append(input[:1] + returnlijst[i])
        return(list)


    if len(input) == 1:
        lijst.append(input[0])
        lijst.append("")
        list.append(input[0])
        list.append("")
        return(lijst)

recurse(input2)

for i in list:
    thing = ""
    for y in range(1, len(i)):
        if len(i) >= 2:
            thing += i[y-1] + " "
    if not len(i) == 0:
        thing += i[len(i)-1]
    list2.append(thing)
        
for i in list2:
    print(i)