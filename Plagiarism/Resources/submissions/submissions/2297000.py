def fibonacci_values(i):
    fib = [0,1]
    for l in range(1,i):
        voriggetal = (i-1)
        tweeterug = (i-2)
        getal = voriggetal + tweeterug
        fib.append(getal)
        tweeterug = voriggetal
        voriggetal = getal
    

        