def quick_sort(l):
    list = l
    pivot = len(list-1)//2
    
    if len(list) == 1:
        return list
    if len(list) == 2:
        return list.sort()
    if len(list) == 3:
        return list.sort()
    
    
    returnlist = []
    smallerlist = []
    biggerlist = []
    piv = list[pivot]
    list.del[pivot]
    for i in range(len(list)):
        if list[i] < piv:
            smallerlist.append(list[i])
    smallerlist = sort(biggerlist)
    
    
    for i in range(len(list)):
        if list[i] > piv:
            biggerlist.append(list[i])
    biggerlist = sort(biggerlist)
    
    returnlist.append(smallerlist)
    returnlist.append(piv)
    returnlist.append(biggerlist)
    
    return returnlist


    