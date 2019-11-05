def fibonacci_values(i):
    fibonaccilijst = [0, 1]
    teller = 2
    for j in range(2, i):
        getal = fibonaccilijst[teller-1] + fibonaccilijst[teller-2]
        teller += 1
        fibonaccilijst.append(getal)
    return fibonaccilijst