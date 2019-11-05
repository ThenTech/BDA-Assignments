cent1 = input("")
cent2 = input("")
cent5 = input("")
cent10 = input("")
cent20 = input("")

cent1 = int(cent1) * 1
cent2 = int(cent2) * 2
cent5 = int(cent5) * 5
cent10 = int(cent10) * 10
cent20 = int(cent20) * 20

euro = cent1 + cent2 + cent5 + cent10 + cent20
euro = euro/100
print("You have", euro, "euro!")
