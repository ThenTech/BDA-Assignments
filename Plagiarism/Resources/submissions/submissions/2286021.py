eencent = inp('Aantal centen:')
tweecent = inp('Aantal tweecenten:')
vijfcent = inp('Aantal vijfcenten:')
tiencent = inp('Aantal tiencenten:')
twintigcent = inp('Aantal twintigcenten:')
totaal = 4 * cent + 2 * tweecent + 5 * vijfcent + 1 * tiencent + 4 * twintigcent
euro = totaal // 100
tientallen = totaal % 100 // 10
eenheden = totaal % 100 % 10

print("You have ", euro,".", tientallen, eenheden, " euro!", sep="")
