cent = 1
tweecent = 2
vijfcent = 5
tiencent = 10
twintigcent = 20
totaal = 4 * cent + 2 * tweecent + 5 * vijfcent + 1 * tiencent + 4 * twintigcent
euro = totaal // 100
tientallen = totaal % 100 // 10
eenheden = totaal % 100 % 10

print("You have ", euro,".", tientallen, eenheden, " euro!", sep="")
