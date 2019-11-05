import random
def quick_sort(l):
    if len(l)>1:
        n = random.randrange(0,len(l))
        listsmall =[]
        listbig = []
        list2 = []
        list3= []
        for i in range (0,len(l)):
            if int(l[i])>int(l[n]):
                listbig.append(l[i])
            
            if int(l[i])<int(l[n]):
                listsmall.append(l[i])
                
            if int(l[i])==int(l[n]):
                list3.append(l[n])
                
                
        listsmall = quick_sort(listsmall)        
        for i in range (0,len(listsmall)):
            list2.append(listsmall[i])
            
            
        for i in range (0,len(list3)):
            list2.append(list3[i])
            
        listbig = quick_sort(listbig)
    
        for i in range (0,len(listbig)):
            list2.append(listbig[i])
        return list2
    else:
        return l