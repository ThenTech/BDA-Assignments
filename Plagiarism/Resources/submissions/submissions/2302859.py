def is_magic_square(matrix):
    #SOM
    som = 0
    for getal in matrix[0]:
        som += getal

    #UNIEKHEIDGETALLEN
    legelijst = []
    for lijst in matrix:
        for getal in lijst:
            if getal in legelijst:
                return False
            else:
                legelijst.append(getal)


    #AANTALRIJENENKOLOMMENGELIJK
    rijen = 0
    kolommen = 0
    for lijst in matrix:
        rijen += 1
        for getal in lijst:
            kolommen += 1
    if rijen != kolommen/rijen:
        return False


    #HORIZONTAAL
    for lijst in matrix:
        testsom = 0
        for getal in lijst:
            testsom += getal
        if som != testsom:
            return False

    #VERTICAAL
    teller = -1
    for x in matrix[0]:
        testsom = 0
        teller += 1
        for lijst in matrix:
            testsom += lijst[teller]
        if som != testsom:
            return False

    #DIAGONAALLBRO
    testsom = 0
    welkelijst = -1
    for lijst in matrix:
        welkelijst += 1
        for plaats in lijst[welkelijst:welkelijst+1]:
            testsom += plaats
    if testsom != som:
        return False
    return True

print(is_magic_square([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))