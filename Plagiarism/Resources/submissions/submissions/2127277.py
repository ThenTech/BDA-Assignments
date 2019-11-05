#Vragen van aantal muntjes
een = int(input("1: "))
twee = 2 * int(input("2: "))
vijf = 5 * int(input("5: "))
tien = 10 * int(input("10: "))
twintig = 20 * int(input("20: "))
#Uitrekenen van bedrag
som = een + twee + vijf + tien + twintig
bedrag = float(som) / 100
#Totaalbedrag tonen
print("You have", bedrag, "euro!")