def fibonacci_values(i):
    r = int(i)
    lijst = []
    if i == 1:
        lijst.append(0)
        return lijst
    elif i == 2:
        lijst.append(1)
        return lijst
    elif i != 2 and i != 1:
        lijst.append(0)
        lijst.append(1)
        for x in range(1, (r-1)):
            lijst.append((lijst[x - 1]) + lijst[x])
        return lijst