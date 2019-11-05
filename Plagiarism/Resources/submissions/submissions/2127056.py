# write your code here
N1=     int(input("hoeveelheid 1 cent:"))
N2=     int(input("hoeveelheid 2 cent:"))
N5=     int(input("hoeveelheid 5 cent:"))
N10=    int(input("hoeveelheid 10 cent:"))
N20=    int(input("hoeveelheid 20 cent:"))
totaal= str(N1 + N2*2 + N5*5 + N10*10 + N20*20)
getal= totaal[len(totaal)-1]
tiental= totaal[len(totaal)-2]
euros= totaal[0]
print("You have ", euros, ".", tiental, getal, " euro!", sep="")