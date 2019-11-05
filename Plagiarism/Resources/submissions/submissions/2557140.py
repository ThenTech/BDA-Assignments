dag_vroeger = input("")
maand_vroeger = input("")
jaar_vroeger = input("")
dag_nu = input("")
maand_nu = input("")
jaar_nu = input("")

if maand_vroeger == maand_nu:
    if dag_nu >= dag_vroeger:
        leeftijd = jaar_nu - jaar_vroeger
    else:
        leeftijd = jaar_nu - jaar_vroeger - 1
elif maand_nu > maand_vroeger:
    leeftijd = jaar_nu - jaar_vroeger
else:
    leeftijd = jaar_nu - jaar_vroeger - 1