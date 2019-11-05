def is_magic_square(matrix):
    #oneven checken
    lengte = len(matrix)
    if lengte % 2 ==0:
        return False
    for el in matrix:
        if len(el) != lengte:
            return False


    # berekent de sommen van de rijen en vgl + unieke el bijvoegen
    unieke_el = []
    lengte = len(matrix[0])
    sommen = []
    for el in range(lengte):
        som = 0
        for index in range(lengte):
            if matrix[el][index] in unieke_el:
                return False
            som = som + matrix[el][index]
            unieke_el.append(matrix[el][index])

    for som_index in range(len(sommen)-1):
        if sommen[som_index] != sommen[som_index+1]:
            return False

    #diagonaal nakijken
    dia_som = []
    for mat in range(lengte):
        dia_som = dia_som + matrix[mat][lengte-1-mat]
    for index in range(len(dia_som) - 1):
        if dia_som[index] != dia_som[index + 1]:
            return False
    return True

