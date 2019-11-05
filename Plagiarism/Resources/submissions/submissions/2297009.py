def is_unique(list):
    for i in range(len(list)):
        for y in range(len(list[i])):
            occurences = 0
            item = list[i][y]
            for i1 in range(len(list)):
                for y1 in range(len(list[i1])):
                    if item == list[i1][y1]:
                        occurences += 1
                        if occurences > 1:
                            return False

    return True

def sum(type, number, list):
    sum = 0
    if type == "row":
        for value in range(len(list[number])):
            sum += value
    if type == "collumn":
        for rows in range(len(list)):
            list[rows][number]
    if type == "diagonal":
        for i in range(len(list)):
            sum += list[i][i]
    
    return sum



def is_magic_square(matrix):
    n = len(matrix) - 1
    if not is_unique(matrix):
        return False
    
    for i in range(n):
        if not (sum("row", n, matrix) == sum("collumn", n, matrix) and sum("collumn", n, matrix) == sum("diagonal", n, matrix)):
            return False
            
    return True