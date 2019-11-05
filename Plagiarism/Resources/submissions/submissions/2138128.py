alfabet = "abcdefghijklmnopqrstuvwxyz"
woord = input("welk woord")
i=0
j=-1
aantletters = 0
letter="a"
while (i<len(alfabet)):
    while (j<len(woord)):
        j+=1
        if (alfabet[i]=woord[j]):
            aantletters+=1
    i+=1
    letter=alfabet[i]+":"
    print (letter, aantalletters )
    