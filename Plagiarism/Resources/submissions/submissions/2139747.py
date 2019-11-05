day= input("geef dag")
maand= input("geef maand")
jaar= input("geef jaar")
day= int(day)
maand= int(maand)
jaar= int(jaar)

day2= input("geefdag2")
maand2= input("geefmaand2")
jaar2= input("geefjaar2")
day2=int(day2)
maand2= int(maand2)
jaar2= int(jaar2)

aantaljaar= jaar-jaar2
if (maand>maand2):
    aantaljaar-= 1
elif (maand==maand2):
    if (dag>dag2):
       aantaljaar-= 1
print(aantaljaar)