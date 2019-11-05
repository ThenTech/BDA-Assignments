def is_magic_square(matrix):
    digits = []
    for row in matrix:
        temp = 0
        for digit in row:
            temp += int(digit)
        digits.append(temp)

    if len(matrix) <= 1:
        for record in digits:
            if 15 != int(record):
                return False
        return True

    for column in range(len(matrix)):
        temp = 0
        for row in range(len(matrix[0])):
            temp += matrix[column][row]
        digits.append(temp)
    
    counter = 0
    temp = 0
    for row in range(len(matrix[0])):
        temp += matrix[counter][row]
        counter += 1
    digits.append(temp)
        
    for record in digits:
        if 15 != int(record):
            return False
    return True
