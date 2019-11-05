def fibonacci_values(i):
    lijst = [0, 1]
    for x in range(1, i-1):
        lijst.append(lijst[x-1] + lijst[x])
    return lijst