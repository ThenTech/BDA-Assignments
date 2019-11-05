cent1 = float(input("ik heb x aantal 1 eurocenten "))
cent2 = float(input("ik heb x aantal 2 eurocenten ")) * 2
cent5 = float(input("ik heb x aantal 5 eurocenten ")) * 5
cent10 = int(input("ik heb x aantal 10 eurocenten ")) * 10
cent20 = int(input("ik heb x aantal 20 eurocenten ")) * 20
euro = (cent1 + cent2 + cent5 + cent10 + cent20) // 100
eurocent = float((cent1 + cent2 + cent5 + cent10 + cent20) % 100)
1 = eurocent[0]
2 = eurocent[1]

print("You have ", int(euro), ".", int(1),2, " euro!", sep="")