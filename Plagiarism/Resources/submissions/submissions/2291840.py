def fibonacci_values(i):
    y = [0,1]
    for x in range(i-2):
        y.append(y[x]+y[x+1])
    
    return y