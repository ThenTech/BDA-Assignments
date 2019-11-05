dag1 = int(input("geef de eerste dag in: "))
maand1 = int(input("geef de eerste maand in"))
jaar1 = int(input("geef het eerste jaaar in"))
dag2 = int(input("geef de momentele dag in"))
maand2 = int(input("geef de momentele maand in"))
jaar2 = int(input("geef het momenele jaar in"))
if dag1 > 31 or dag2 > 31:
    print("dag moet kleiner zijn dan 31")
if maand1 > 12 or maand2 > 12:
    print("maand moet kleiner zijn dan 12")
if dag1 < dag2:
    if maand1 < maand2:
        print((abs(jaar2 - jaar1)))
    elif maand1 >= maand2:
        print(abs(jaar2 - jaar1+1))
else:
    if maand1 < maand2:
        print(abs(jaar2 - jaar1))
    elif maand1 >= maand2:
        print(abs(jaar2 - jaar1+1))
print()