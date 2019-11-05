def fibonacci_values(i):
    lijst = [0, 1]
    waarde = 0
    for y in range(2, i):
        waarde = lijst[y-1] + lijst[y-2]
        lijst.append(waarde)
    return lijst