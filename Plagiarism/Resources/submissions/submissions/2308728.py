def lucky_numbers(n):
    getallen = [x for x in range(1,n+1)]
    kopie = getallen[:]
    zoekkopie = getallen[:]
    verwijderen = ""
    deler = 2
    startpos = 1
    while deler < len(kopie) :#len(kopie)
        zoekkopie = kopie[:]
        for index in range(len(zoekkopie)//deler): # teller, die start met 2
            verwijderen = (zoekkopie[startpos +(index*deler)])
            print (verwijderen)
            for x in range(len(kopie)):
                if kopie[x] == verwijderen:
                    del kopie[x]
                    print(kopie)
                    break
        deler = deler + 1
        startpos = startpos + 1