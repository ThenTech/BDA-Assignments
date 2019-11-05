birth_dag = int(input("Dag: "))
birth_maand = int(input("Maand: "))
birth_jaar = int(input("Jaar: "))
nu_dag = int(input("Dag: "))
nu_maand = int(input("Maand: "))
nu_jaar = int(input("Jaar: "))

Leeftijd = nu_jaar - birth_jaar

if (birth_dag + 31*birth_maand >= nu_dag + 31*nu_maand):
    print(Leeftijd - 1)
else:
    print(Leeftijd)