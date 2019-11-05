def is_magic_square(matrix):
    lengte = len(matrix)
    lengte2 = len(matrix[0])
    som = 0
    som2 = 0
    uitkomst = True
    for i in range(lengte2):
        som += matrix[0][i]
    for j in range(1,lengte):
        for i in range(lengte2):
            som2 += matrix[j][i]
        if som2 == som:
            uitkomst = uitkomst and True
        else:
            uitkomst = uitkomst and False
        som2 = 0
    for j in range(lengte2):
        for i in range(lengte):
            som2 += matrix[i][i]
        if som2 == som:
            uitkomst = uitkomst and True
        else:
            uitkomst = uitkomst and False
        som2 = 0
    return uitkomst