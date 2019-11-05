cent1 = int(input("Aantal 1 cent = ?"))
cent2 = int(input("Aantal 2 cent = ?"))
cent5 = int(input("Aantal 5 cent = ?"))
cent10 = int(input("Aantal 10 cent = ?"))
cent20 = int(input("Aantal 20 cent = ?"))

totaal = cent1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20

print("You have " + str(totaal/100) + " euro!")
