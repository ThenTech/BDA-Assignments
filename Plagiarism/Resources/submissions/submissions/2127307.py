totaal_bedrag = int(input('Wat bedrag heb je? ')) # in cent
aantal_twee_euro = totaal_bedrag // 200
aantal_een_euro = (totaal_bedrag%200)//100
aantal_vijftigc =((totaal_bedrag%200)%100) //50
aantal_twintigc = (((totaal_bedrag%200)%100)%50) //20
aantal_tienc = 0
aantal_vijfc = 0
aantal_tweec = 0
aantal_eenc = 0
overige = totaal_bedrag%200%100%50%20
if overige > 10:
    aantal_tienc = 1
    aantal_vijfc = (overige % 10) // 5
    aantal_tweec = ((overige%10)%5) // 2
    aantal_eenc = (((overige%10)%5)%2)
else:
    aantal_tienc = 0
    aantal_vijfc = (overige % 10) // 5
    aantal_tweec = ((overige%10)%5) // 2
    aantal_eenc = (((overige%10)%5)%2)
print("2-euros:", aantal_twee_euro)
print("1-euros:", aantal_een_euro)
print("50c-euros:", aantal_vijftigc)
print("20c-euros", aantal_twintigc)
print("10c-euros", aantal_tienc)
print("5c-euros", aantal_vijfc)
print("2c-euros:", aantal_tweec)
print("1c-euros", aantal_eenc)
