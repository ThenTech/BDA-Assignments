def encode(string):
    index = -1
    oplossing = ''
    lengte = len(string)
    for teken in string:
        index += 1
        getal = 0
        if index == 0:
            if lengte > 1:
                if string[index+1] == "X":
                    getal += 1
                else:
                    continue
        elif index == (lengte - 1):
            if string[index-1] == "X":
                getal += 1
        else:
            if string[index-1] == "X":
                getal += 1
            if string[index+1] == "X":
                getal += 1
        oplossing = oplossing + str(getal)
    return oplossing


def decode(string):
    oplossing = ' ' * len(string)
    oplossing2 = ' ' * len(string)
    oplossinglijst = []
    index = -1
    for teken in string:
        index += 1
        if index == 0:
            if teken == "1":
                oplossing[index+1] = "X"
                oplossing2[index+1] = "X"
        elif 0 < index < (len(string)-2):
            if teken == "2":
                oplossing[index-1] = "X"
                oplossing2[index-1] = "X"
                oplossing[index+1] = "X"
                oplossing2[index+1] = "X"
            if teken == "1":
                if oplossing[index-1] == " " and oplossing[index+1] == " ":
                    oplossing[index+1] = "X"
                    oplossing2[index-1] = "X"
            
    
    if string == encode(oplossing):
        oplossinglijst.append(oplossing)
        oplossinglijst.append(oplossing2)
        
    return oplossinglijst