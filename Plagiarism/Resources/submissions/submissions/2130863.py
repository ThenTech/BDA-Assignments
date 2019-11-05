# 42514
cent1 = int(input("Aantal 1 cent = ?"))
cent2 = int(input("Aantal 2 cent = ?"))
cent5 = int(input("Aantal 5 cent = ?"))
cent10 = int(input("Aantal 10 cent = ?"))
cent20 = int(input("Aantal 20 cent = ?"))

totaal = cent1 + cent2 * 2 + cent5 * 5 + cent10 * 10 + cent20 * 20

eenh = int(totaal / 100)
tient = int(totaal / 10) % 10
honderdt = int((totaal/10 - int(totaal/10))*10)

print("You have ", eenh, ".", tient, honderdt, " euro!", sep="")
