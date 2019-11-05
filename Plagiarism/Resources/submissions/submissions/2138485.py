# write your code here
woord1=input()
woord2= input()
lengthe1=len(woord1)
lengthe2=len(woord2)
i=0
aantal1=0
aantal2=0
juistheid=True
for x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRESTUVWXYZ":
    i=0
    aantal1=0
    while i+1< lengthe+1:
        if woord[i] == x:
           aantal1+=1
            i+=1
        elif i+1 == lengthe:
            i+=1
        else:
            i+=1
    aantal2=0
    i=0
    while i+1< lengthe+1:
        if woord[i] == x:
            aantal2+=1
            i+=1
        elif i+1 == lengthe:
            i+=1
        else:
            i+=1
    if aantal1 != aantal2:
        juistheid = juistheid and False
if juistheid == False:
    print(woord1, "and", woord2,"are not anagrams")
else:
    print(woord1, "and", woord2, "are not anagrams")
        
    