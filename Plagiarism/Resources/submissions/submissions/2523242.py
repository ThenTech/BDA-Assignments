import random
def quick_sort(l):
    if len(l)>1:
        n = random.range(0,len(l))
        listsmall =[]
        listbig = []
        list2 = []
        for i in range (0,len(l)):
            if int(l[i])>int(l[n]):
                listbig.append(l[i])
            
            if int(l[i])<int(l[n]):
                listsmall.append(l[i])
            
        listsmall = quick_sort(listsmall)        
        for i in range (0,len(listsmall)):
            list2.append(listsmall[i])
        list2.append(l[n])
        listbig = quicksort(listbig)
    
        for i in range (0,len(listbig)):
            list2.append(listbig[i])
        return list2
    else:
        return l