alfabet = "abcdefghijklmnopqrstuvwxyz"
woord = input("welk woord")
woord2 = input("welk woord nu weer")
i=0
j=-1
k=-1
aantletters = 0
aantletters2 = 0

while (i<len(alfabet)):
    while (j<len(woord)-1):
        j+=1
        if (alfabet[i]==woord[j]):
            aantletters+=1
    while (k<len(woord2)-1):
        j+=1
        if (alfabet[i]==woord2[k]):
            aantletters2+=1
    if (aantletters != aantletters2):
       print (woord,"and", woord2,"are not anagrams")
       break
    i+=1
    aantletters=0
    aantletters2 = 0
    j=-1
    k=-1
if (i<len(alfabet)):
    print (woord,"and", woord2,"are anagrams")