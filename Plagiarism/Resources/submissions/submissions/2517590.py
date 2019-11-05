def merge_lists(first,second):
    i=0
    j=0
    tirth =[]
    while i<len(first) and j<len(second):
        if int(first[i])<int(second[j]):
            tirth.append (first[i])
            i+=1
        if int(first[i])>int(second[j]):
            tirth.append (second[j])
            j+=1
    for k in range (i,len(first)):
        tirth.append(first[k])
    for h in range (j, len(second)):
        tirth.append(second[h])
    return(tirth)

def merge_sort(list):
    list1=[]
    list2=[]
    if len(list)<=1:
        return list
    elif len(list)>1:
        for i in range(0:len(list)/2):
            list1.append(list[i])
            def merge_sort(list1)
        for i in range(len(list)/2:len(list)):
            list2.append(list[i])
            def merge_sort(list2)
        list=merge_lists(list1,list2)
        return list
        