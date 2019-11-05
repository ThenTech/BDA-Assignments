dag_vroeger = int(input(""))
maand_vroeger = int(input(""))
jaar_vroeger = int(input(""))
dag_nu = int(input(""))
maand_nu = int(input(""))
jaar_nu = int(input(""))

if maand_vroeger == maand_nu:
    if dag_nu >= dag_vroeger:
        leeftijd = jaar_nu - jaar_vroeger
    else:
        leeftijd = jaar_nu - jaar_vroeger - 1
elif maand_nu > maand_vroeger:
    leeftijd = jaar_nu - jaar_vroeger
else:
    leeftijd = jaar_nu - jaar_vroeger - 1
print(leeftijd)