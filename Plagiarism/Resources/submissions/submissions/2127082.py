# write your code here
N1 =     int(input("hoeveelheid 1 cent:"))
N2 =     int(input("hoeveelheid 2 cent:"))
N5 =     int(input("hoeveelheid 5 cent:"))
N10 =    int(input("hoeveelheid 10 cent:"))
N20 =    int(input("hoeveelheid 20 cent:"))
totaal = str(N1 + N2*2 + N5*5 + N10*10 + N20*20)
getal = totaal[len(totaal)-1]
tiental = totaal[len(totaal)-2]
euros = int(N1*0.01 + N2*0.02 + N5*0.05 + N10*0.10 + N20*0.20)
print("You have ", euros, ".", tiental, getal, " euro!", sep="")