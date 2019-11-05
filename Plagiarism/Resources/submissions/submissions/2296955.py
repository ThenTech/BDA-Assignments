def fibonacci_values(i):
    rij_van_fibonacci = [0, 1]
    vorig_getal = 1
    twee_getallen_terug = 0

    for j in range(2, i):
        getal = vorig_getal + twee_getallen_terug
        rij_van_fibonacci.append(getal)

        twee_getallen_terug = vorig_getal
        vorig_getal =getal

    return  rij_van_fibonacci