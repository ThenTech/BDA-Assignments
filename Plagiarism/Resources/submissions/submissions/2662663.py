def is_magic_square(matrix):
    if len(matrix)%2 != 1 or len(matrix[0])%2 != 1:
        return False
    correctsum = 0
    for item in matrix[0]:
        correctsum += int(item)
    
    
    for row in range(len(matrix)):
        currentsum = 0
        for column in range(len(matrix[row]))
            currentsum += int(matrix[row][column])
            
        if not currentsum = sum:
            return False
            
    for column in range(len(matrix[0])):
        currentsum = 0
        for row in range(len(matrix)):
            currentsum += int(matrix[row][column])
        
        if not currentsum = sum:
            return False
    
            
    
            