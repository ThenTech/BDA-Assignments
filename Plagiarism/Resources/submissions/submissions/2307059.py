def is_magic_square(matrix):
    checkofuniek = list()
    verticaal = list()
    verticaalsommen = list()
    linksschuin = list()
    rechtsschuin = list()
    for i in matrix:
        for j in i:
            checkofuniek.append(j)
    if is_unique(checkofuniek):
        if (len(matrix) == 1 and len(matrix[0]) == 1) or (len(matrix) % 2 == 1 and len(matrix) == len(matrix[0])):
            for i in matrix:
                if sum(i) == sum(matrix[0]):
                    continue
                else:
                    return False
            teller = 0
            while teller < len(matrix[0]):
                teller = 0
                for i in matrix:
                    verticaal.append(i[teller])
                teller += 1
                verticaalsommen.append(sum(verticaal))
                for i in verticaal:
                    verticaal.remove(i)
            if len(verticaalsommen) == 1 or (not is_unique(verticaalsommen)):
                teller2 = 0
                while teller2 < len(matrix[0]):
                    for i in matrix:
                        linksschuin.append(i[0+teller2])
                        rechtsschuin.append(i[len(i)-1-teller2])
                        teller2 += 1
                if sum(rechtsschuin) == sum(linksschuin) == sum(matrix[0]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def is_unique(l):
    teller1 = 0
    for i in l:
        teller2 = 0
        for j in l:
            if teller1 != teller2 and i == j:
                return False
            else:
                teller2 += 1
        teller1 += 1
    return True