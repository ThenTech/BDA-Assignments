def fibonacci_values(i):
    fib_list = [0, 1]
    for x in range(2, i + 1):
        vorig_getal = fib_list[x - 1]
        vorig_getal2 = fib_list[x - 2]
        x = vorig_getal + vorig_getal2
        fib_list.append(x)
    print(fib_list)