daggeboren = int(input(''))
maandgeboren = int(input(''))
jaargeboren = int(input(''))
dagvandaag = int(input(''))
maandvandaag = int(input(''))
jaarvandaag = int(input(''))

leeftijd = jaarvandaag - jaargeboren
if maandvandaag < maandgeboren:
        leeftijd = leeftijd - 1
elif maandvandaag == maandgeboren:
    if dagvandaag < daggeboren:
        leeftijd = leeftijd - 1
print(leeftijd)