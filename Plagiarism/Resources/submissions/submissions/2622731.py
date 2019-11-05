def encode(string):
    index = -1
    oplossing = ''
    lengte = len(string)
    for teken in string:
        index += 1
        getal = 0
        if index == 0:
            if string[index+1] == "X":
                getal += 1
        if index == lengte - 1:
            if string[index-1] == "X":
                getal += 1
        else:
            if string[index-1] == "X":
                getal += 1
            if string[index+1] == "X":
                getal += 1
        oplossing = oplossing + str(getal)


def decode(s):
    pass