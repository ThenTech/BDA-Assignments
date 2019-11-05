set = input("geef set")
listsubsets = [" "]


def maaksubset(set, listsubsets):
    subset = set[len(set)-1:]+" "
    set = set[0:len(set)-2]
    for i in range (0,len(listsubsets)):
        print (subset+listsubsets[i])

    listsubsets.append (subset)
    if len(set)>=1:
        maaksubset(set,listsubsets)
    
maaksubset (set,listsubsets)