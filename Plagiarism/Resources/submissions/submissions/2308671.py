#maak een lijst met de te verwijderen getallen
#verwijderen deze uit de kopie
#repeat

def lucky_numbers(n):
    getallen = [x for x in range(1,n+1)]
    kopie = getallen[:]
    verwijderen = ""
    teller = 0
    while teller < 1 :#len(kopie)
        for index in range(len(getallen)//2): # teller, die start met 2
            verwijderen = (getallen[1 +(index*2)])
            print (verwijderen)
            for x in range(len(kopie)):
                if kopie[x] == verwijderen:
                    del kopie[x]
                    print(kopie)
                    break
        teller = teller + 1


    return verwijderen


print(lucky_numbers(22))