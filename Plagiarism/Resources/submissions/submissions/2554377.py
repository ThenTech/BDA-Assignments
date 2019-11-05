bday = int(input("Bday: "))
bmonth = int(input("Bmonth: "))
byear = int(input("Byear: "))

nday = int(input("Nday: "))
nmonth = int(input("Nmonth: "))
nyear = int(input("Nyear: "))

leeftijd = nyear - byear

if bday > nday and bmonth > nmonth:
    leeftijd -= 1

print(leeftijd)