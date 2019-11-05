dag1 = int(input("Wat is de geboortedag van persoon: "))
maand1 = int(input("Wat is de geboortemaand van persoon: "))
jaar1 = int(input("Wat is het geboortejaar van persoon: "))
dag2 = int(input("Wat is de huidige dag: "))
maand2 = int(input("Wat is de huidige maand: "))
jaar2 = int(input("Wat is het huidige jaar: "))
ouderdom = jaar2 - jaar1
if maand1 > maand2:
    ouderdom -= 1
elif maand1 = maand2:
    if dag1 > dag2:
        ouderdom -= 1
print(ouderdom)
        
