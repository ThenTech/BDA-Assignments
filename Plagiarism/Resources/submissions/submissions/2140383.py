dag =int(input("geef dag geboren: "))
maand =int(input("geef maand geboren"))
jaar = int(input("geef jaar geboren"))
dag_nu = int(input("geef huidige dag"))
maand_nu = int(input("geef huidige maand"))
jaar_nu = int(input("geef huidige jaar"))
leeftijd=0
if maand_nu < maand:
    leeftijd = jaar - jaar_nu -1
elif maand_nu = maand:
    if dag_nu >= dag:
        leeftijd = jaar - jaar_nu
    else:
        leeftijd = jaar - jaar_nu -1
else:
    leeftijd = jaar - jaar_nu
print(leeftijd)