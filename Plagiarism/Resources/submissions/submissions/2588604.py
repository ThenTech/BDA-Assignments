def is_magic_square(matrix):
    if is_verschillend(matrix) == False:
        return False
    else:
        #checken of het een n x n matrix is
        if len(matrix) != len(matrix[0]):
            return False
        
        sommen = list()

        #rijen
        for i in matrix:
            sommen.append(sum(i))

        #kolommen
        for i in range(len(matrix[0])):
            kolommensom = list()
            for j in matrix:
                kolommensom.append(j[i])
            sommen.append(sum(kolommensom))

        #diagonalen
        linksbovendiagonaal = list()
        for i in range(len(matrix[0])):
            linksbovendiagonaal.append(matrix[i][i])
        rechtsbovendiagonaal = list()
        for i in range(len(matrix[0])):
            rechtsbovendiagonaal.append(matrix[i][len(matrix[0])-1-i])
        sommen.append(sum(linksbovendiagonaal))
        sommen.append(sum(rechtsbovendiagonaal))

        #checken
        for i in sommen:
            if i != sommen[0]:
                return False
        return True

def is_verschillend(matrix):
    verschillendteller = 0
    for i in matrix:
        for j in i:
            tweedeverschillendteller = 0
            for x in matrix:
                for z in x:
                    if j == z and verschillendteller != tweedeverschillendteller:
                        return False
                    tweedeverschillendteller += 1
            verschillendteller += 1