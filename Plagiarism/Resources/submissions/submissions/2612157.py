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
    #lege lijst aanmaken om aan te passen
    minefield = list()
    for i in range(len(string)):
        minefield.append(" ")

    #eerste en laatste staan sowieso al vast
    if string[0] == "1":
        minefield[1] = "X"
    if string[len(string)-1] == "1":
        minefield[len(minefield)-2] = "X"

    #iedere 2 staat ook sowieso vast
    stringindexteller = 0
    for i in string:
        if i == "2":
            minefield[stringindexteller+1] = "X"
            minefield[stringindexteller-1] = "X"
        stringindexteller += 1

    #nu de rest, heeft meestal meerdere mogelijkheden, maar hangt volgens mij van de eerste al af...
    indexteller = 0
    for i in string:
        if indexteller == 0 or indexteller == len(string)-1:
            indexteller += 1
            pass
        else:
            #eerste
            if i == "1" and minefield[indexteller-1] != "X" and minefield[indexteller+1] != "X":
                tweede_mogelijkheid = minefield[:]
                minefield[indexteller-1] = "X"
                tweede_mogelijkheid[indexteller+1] = "X"

                #nog verder aanpassen
                fouteteller = 0
                fouteindex = list()
                for i in range(len(string)):
                    if string[i] != encode(minefield)[i]:
                        minefield[i + 1] = "X"



                foutefouteteller = 0
                foutefouteindex = list()
                for i in range(len(string)):
                    if string[i] != encode(tweede_mogelijkheid)[i]:
                        foutefouteteller += 1
                        foutefouteindex.append(i)

                if foutefouteteller < 2:
                    tweede_mogelijkheid[i-1] = "X"
                else:
                    tweede_mogelijkheid[foutefouteindex[len(foutefouteindex)-1]-1] = "X"

    minefieldstring = ""
    tweede_mogelijkheid_string = ""
    for i in minefield:
        minefieldstring += i
    for i in tweede_mogelijkheid:
        tweede_mogelijkheid_string += i


    print(tweede_mogelijkheid_string)
    return minefieldstring