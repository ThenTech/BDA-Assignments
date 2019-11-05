# write your code here
woord1=input()
woord2= input()
lengthe1=len(woord1)
lengthe2=len(woord2)
i=0
aantal1=0
aantal2=0
if lengthe1!=lengthe2:
    print(woord1,"and",woord2,"are not anagrams")
else:
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
        print(woord1,"and",woord2,"are not anagrams")

