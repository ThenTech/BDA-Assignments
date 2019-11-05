def fibonacci_values(i):
    fibonacci = [0, 1]
    for x in range(0,int(i-2)):
        getal = fibonacci[x] + fibonacci[x+1]
        fibonacci.append(getal)
    return fibonacci
