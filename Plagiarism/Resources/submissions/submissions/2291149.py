def fibonacci_values(i):
    list = [0,1]
    som = 1
    for j in range(2,i):
        list.append(som)
        laatste = list[j]
        vorige = list[j-1]
        som = laatste + vorige
    return list