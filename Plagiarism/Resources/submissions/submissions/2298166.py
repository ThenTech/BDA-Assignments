def is_magic_square(matrix):
    lengte = len(matrix)
    for el in matrix:
        if len(el) != lengte:
            return False

    # berekent de sommen van de rijen en vgl
    lengte = len(matrix[0])
    sommen = []
    for el in range(lengte):
        som = 0
        for index in range(lengte):
            som = som + matrix[el][index]

    for som_index in range(len(sommen)-1):
        if sommen[som_index] != sommen[som_index+1]:
            return False
    return True
