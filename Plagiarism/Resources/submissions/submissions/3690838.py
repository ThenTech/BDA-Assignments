cent1 = float(input("ik heb x aantal 1 eurocenten "))
cent2 = float(input("ik heb x aantal 2 eurocenten ")) * 2
cent5 = float(input("ik heb x aantal 5 eurocenten ")) * 5
cent10 = int(input("ik heb x aantal 10 eurocenten ")) * 10
cent20 = int(input("ik heb x aantal 20 eurocenten ")) * 20
euro = (cent1 + cent2 + cent5 + cent10 + cent20) // 100
eurocent = int((cent1 + cent2 + cent5 + cent10 + cent20) % 100)
print("You have ", int(euro), ".",eurocent, " euro!", sep="")