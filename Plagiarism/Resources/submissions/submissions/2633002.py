string = input()

#string omzetten naar lijst
getallen = string.split(" ")

subsets = list()

def substring(getallen):
    if len(getallen) == 0:
        print("")
    else:
        #recursieve functie openen
        recursie(getallen, subsets)

def recursie(lijst, subsets):
    #als lijst leeg is, moeten we printen
    if len(lijst) == 0:
        #lege lijst moet ook geprint worden
        if len(subsets) == 0:
            print(" ")
        #subset mooi printen
        teller = 0
        for i in subsets:
            if teller == len(subsets)-1:
                print(i)
                teller += 1
            else:
                print(i, end=" ")
                teller += 1
        return

    #eerste getal afzonderen van de rest
    eerste_getal = lijst[0]
    alle_andere_getallen = lijst[1:]

    #subsets maken zonder eerste getal
    recursie(alle_andere_getallen, subsets)

    #subsets maken met eerste getal
    recursie(alle_andere_getallen, subsets + [eerste_getal])

substring(getallen)