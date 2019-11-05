def fibonacci_values(i):
    fib = [0,1]
    for l in range(1,i):
        voriggetal = fib[x-1]
        tweeterug = fib[x-2]
        getal = voriggetal + tweeterug
        fib.append(getal)
        tweeterug = voriggetal
        voriggetal = getal
    

        