set = input("geef set")
listsubsets = [" "]

maaksubset (set,listsubsets)
def maaksubset(set, listsubsets):
    subset = set[len(set)-1]
    set = set[0:len(set)-1]
    for i in range (0,len(listssubsets)):
        print (subset+listsubsets[i])

    listsubsets.append (subset)
    if len(set)>=1:
        maaksubset(set,listsubsets)
    
