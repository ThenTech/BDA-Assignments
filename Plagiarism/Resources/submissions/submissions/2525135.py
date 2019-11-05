cent1 = int(input("Aantal 1 cents: "))
cent2 = int(input("Aantal 2 cents: "))
cent5 = int(input("Aantal 5 cents: "))
cent10 = int(input("Aantal 10 cents: "))
cent20 = int(input("Aantal 20 cents: "))

tot_cent = cent1 + 2*cent2 + 5*cent5 + 10*cent10 + 20*cent20
euros = tot_cent // 100
rem_cent = tot_cent % 100
centiemen = rem_cent // 10
rem_cent = rem_cent % 10
cent = rem_cent // 10

print("You have ", euros, ".", centiemen, cent, " euro!", sep="")