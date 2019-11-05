def fibonacci_values(i):
    fibonacci = [0, 1]
    for item in range(len(fibonacci), i):
        fibonacci += [fibonacci[item - 2] + fibonacci[item - 1]]
        
    return fibonacci