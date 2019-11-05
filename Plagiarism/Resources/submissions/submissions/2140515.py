daybirth = input("Geef een string: ")
monthbirth = input("Geef een string: ")
yearbirth = input("Geef een string: ")
daynow = input("Geef een string: ")
monthnow = input("Geef een string: ")
yearnow = input("Geef een string: ")
if int(monthbirth) - int(monthnow) < 0:
    print(int(yearnow)-int(yearbirth))
elif int(monthbirth) - int(monthnow) == 0:
    if int(daynow)-int(daybirth) >= 0:
        print(int(yearnow) - int(yearbirth))
    else:
        print(int(yearnow) - int(yearbirth) - 1)
else:
    print(int(yearnow)-int(yearbirth)-1)