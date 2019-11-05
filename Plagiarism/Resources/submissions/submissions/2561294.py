def is_unique(matrix):
    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            teller = 0
            getal = matrix[i][x]
            for y in range(len(matrix)):
                for z in range(len(matrix[y])):
                    if matrix[y][z] == getal:
                        teller += 1
                    continue
            if teller > 1:
                return False
            else:
                continue
    return True

def is_magic_square(matrix):
    if is_unique(matrix) is False:
        return False
    else:
        som = 0
        for i in range(len(matrix)):
            som += matrix[i][0]
        #horizontaal
        for i in range(len(matrix)):
            teller = 0
            som2 = 0
            while teller < len(matrix[0]):
                som2 += matrix[i][teller]
                teller += 1
            if som != som2:
                return False
            else:
                continue
        #verticaal
        teller = 0
        while teller < len(matrix[0]):
            som2 = 0
            for i in range(len(matrix)):
                som2 += matrix[i][teller]
            if som != som2:
                return False
            else:
                teller += 1
                continue
        return True
