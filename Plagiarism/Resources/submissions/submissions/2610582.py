def encode(minefield):
    #indexen van bommen en lege vakjes groeperen
    bommen = list()
    leeg = list()
    index = 0
    for i in minefield:
        if i == "X":
            bommen.append(index)
            index += 1
        else:
            leeg.append(index)
            index += 1

    #string maken
    string = ""
    for i in range(len(minefield)):
        toe_te_voegen_getal = 0
        if (i-1) in range(len(minefield)) and (i-1) in bommen:
            toe_te_voegen_getal += 1
        if (i+1) in range(len(minefield)) and (i+1) in bommen:
            toe_te_voegen_getal += 1
        string += str(toe_te_voegen_getal)
    return string


def decode(string):
    pass