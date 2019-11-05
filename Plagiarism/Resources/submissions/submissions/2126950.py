getal = int(input())

Twee = 0
Een = 0
Vijftig = 0
Twintig = 0
Tien = 0
Vijf = 0
TweeCent = 0
EenCent = 0

while getal > 0:
    if getal > 200:
        getal -= 200
        Twee += 1
    elif getal > 100:
        getal -= 100
        Een += 1
    elif getal > 50:
        getal -= 50
        Vijftig += 1
    elif getal > 20:
        getal -= 20
        Twintig += 1
    elif getal > 10:
        getal -= 10
        Tien += 1
    elif getal > 5:
        getal -= 5
        Vijf += 1
    elif getal > 2:
        getal -= 2
        TweeCent += 1
    elif getal > 1:
        getal -= 1
        EenCent += 1
    else:
        break
        
print("2-euros:", Twee, "\n1-euros:", Een, "\n50c-euros:", Vijftig, "\n20c-euros:", Twintig, "\n10c-euros:", Tien, "\n5c-euros:", Vijf, "\n2c-euros:", TweeCent, "\n1c-euros:", EenCent, sep="")