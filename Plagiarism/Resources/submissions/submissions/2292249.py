def fibonacci_values(i):
    list =[0,1]
    for x in range(1,i - 1):
        newnumber = list[x] + list[x-1]
        list.append(newnumber)
        print(list)
        x+=1
    return list