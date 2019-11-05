dag1 = int(input("dag1:"))
maand1 = int(input("maand1:"))
jaar1 = int(input("jaar1:"))
dag2 = int(input("dag2:"))
maand2 = int(input("maand2:"))
jaar2 = int(input("jaar2:"))
global leeftijd
if maand1 < maand2:
    if dag1 < dag2:
        leeftijd = jaar2 - jaar1
else:
    leeftijd = (jaar2 - jaar1) - 1

print(leeftijd)