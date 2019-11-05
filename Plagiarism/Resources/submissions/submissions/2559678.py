def quick_sort(l):
    if len(l) == 0:
        return l
    
    list = l
    pivot = (len(list)-1)//2
 
    
    returnlist = []
    smallerlist = []
    biggerlist = []
    piv = list[pivot]
    del list[pivot]
    for i in range(len(list)):
        if list[i] <= piv:
            smallerlist.append(list[i])
    if len(smallerlist) > 1:
        smallerlist = quick_sort(smallerlist)
    
    
    for i in range(len(list)):
        if list[i] > piv:
            biggerlist.append(list[i])
    if len(biggerlist) > 1:
        biggerlist = quick_sort(biggerlist)
    """  
    if len(smallerlist) > 0:
        returnlist.append(smallerlist)
    returnlist.append(piv)
    if len(biggerlist) > 0:
        returnlist.append(biggerlist)
    """
    pivlist = [piv]
    returnlist = smallerlist + pivlist + biggerlist
    return returnlist
