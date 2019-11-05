def fibonacci_values(i):
    fibonacci_list = []
    getal1 = 0
    getal2 = 1
    for j in range(0, i):
        fibonacci_list.append(getal1)

        hulp_var = getal1
        getal1 = getal2
        getal2 = hulp_var + getal2
    return fibonacci_list
