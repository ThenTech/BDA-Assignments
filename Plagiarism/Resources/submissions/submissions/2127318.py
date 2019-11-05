cent1 = input("")
cent2 = input("aantal 2 cent:")
cent5 = input("aantal 5 cent:")
cent10 = input("aantal 10 cent:")
cent20 = input("aantal 20 cent:")

print(cent1, cent2, cent5, cent10, cent20)

cent1 = int(cent1) * 1
cent2 = int(cent2) * 2
cent5 = int(cent5) * 5
cent10 = int(cent10) * 10
cent20 = int(cent20) * 20

print(cent1, cent2, cent5, cent10, cent20)

euro = cent1 + cent2 + cent5 + cent10 + cent20
euro = euro/100
print(euro)
