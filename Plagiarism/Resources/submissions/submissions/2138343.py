alfabet = "abcdefghijklmnopqrstuvwxyz"
woord = input("welk woord")
i=0
j=-1
aantletters = 0
letter="a"
while (i<len(alfabet)-1):
    while (j<len(woord)-1):
        j+=1
        if (alfabet[i]==woord[j]):
            aantletters+=1
    letter=alfabet[i]+":"
    i+=1
    print (letter, aantletters )
    aantletters=0
    j=-1
    