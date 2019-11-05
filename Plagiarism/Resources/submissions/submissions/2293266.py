def fibonacci_values(i):
    list =[0,1]
    for n in range(2,i):
        list = list+[(list[n-2]+list[n-1])]
    return list   