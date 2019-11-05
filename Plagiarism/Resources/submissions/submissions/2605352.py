def plaats_in_woord(lengte, getal):
    plaatsinwoord = getal % lengte
    return plaatsinwoord

def create_sequence(zin, begin, einde):
    lengte = len(zin)
    for x in range(begin, einde+1):
        plaats = plaats_in_woord(lengte, x)
        print(zin[plaats], end="")

#create_sequence("word", -3, 9)