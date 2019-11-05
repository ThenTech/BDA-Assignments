def fibonacci_values(i):
    i[0] = 0
    i[1] = 1 
    for value in range(1, i-2):
        i[value+2] = i[value + 1] +i[value]
        
        