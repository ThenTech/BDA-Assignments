dag1 = int(input('Geboortedag: '))
maand1 = int(input('Geboortemaand: '))
jaar1 = int(input('Geboortejaar'))
dag2 = int(input('huidige dag: '))
maand2 = int(input('huidige maand: '))
jaar2 = int(input('huidig jaar'))
jaren = jaar2 - jaar1
if maand2 > maand1:
    print(jaren)
elif maand2 < maand1:
    print(jaren-1)
elif maand1 == maand2:
    if dag2 > dag1:
        print(jaren-1)
    elif dag2 < dag1:
        print(jaren)
    else:
        print(jaren)