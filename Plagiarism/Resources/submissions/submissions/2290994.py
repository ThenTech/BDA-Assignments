def fibonacci_values(i):
    list = [1,1]
    som = 2
    for j in range(3,i):
        list.append(som)
        laatste = list[j-2]
        vorige = list[j-1]
        som = laatste + vorige
    return list