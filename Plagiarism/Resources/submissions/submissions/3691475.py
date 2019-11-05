aantal_twintig=int(input("hoeveel 20 cent muntjes?: "))
aantal_tien=int(input("hoeveel 10 cent muntjes?: "))
aantal_vijf=int(input("hoeveel 5 cent muntjes?: "))
aantal_twee=int(input("hoeveel 2 cent muntjes?: "))
aantal_een=int(input("hoeveel 1 cent muntjes?: "))
geld=(aantal_twintig*20)+(aantal_tien*10)+(aantal_vijf*5)+(aantal_twee*2)+(aantal_een*1)
if geld<100:
    print("je hebt 0.", geld, " euro", sep="")
else:
    print("je hebt", geld/10, ".") #nog delen door tien of zoiets, nog niet af