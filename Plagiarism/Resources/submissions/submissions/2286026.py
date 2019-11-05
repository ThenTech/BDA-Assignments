eencent = input('Aantal centen:')
tweecent = input('Aantal tweecenten:')
vijfcent = input('Aantal vijfcenten:')
tiencent = input('Aantal tiencenten:')
twintigcent = input('Aantal twintigcenten:')
totaal = 4 * cent + 2 * tweecent + 5 * vijfcent + 1 * tiencent + 4 * twintigcent
euro = totaal // 100
tientallen = totaal % 100 // 10
eenheden = totaal % 100 % 10

print("You have ", euro,".", tientallen, eenheden, " euro!", sep="")
