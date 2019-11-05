#Vragen van aantal muntjes
een= int(input("1: "))
twee= 2 * int(input("2: "))
vijf= 5 * int(input("5: "))
tien= 10 * int(input("10: "))
twintig= 20 * int(input("20: "))
vijftig= 50 * int(input("50: "))
#Uitrekenen van bedrag
som = een + twee + vijf + tien + twintig + vijftig
bedrag = float(som) / 100
#Totaalbedrag tonen
print("You have", bedrag, "euro!")