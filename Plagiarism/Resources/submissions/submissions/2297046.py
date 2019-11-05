def fibonacci_values(i):
    fib = [0,1]
    for i in range(1, i):
        voriggetal = fib[i-1]
        tweeterug = fib[i-2]
        getal = voriggetal + tweeterug
        fib.append(getal)
        tweeterug = voriggetal
        voriggetal = getal
    

        