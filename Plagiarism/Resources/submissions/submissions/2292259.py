def fibonacci_values(i):
    list =[0,1]
    for x in range(1,i - 1):
        list.append(list[x] + list[x-1])
        x+=1
    return list