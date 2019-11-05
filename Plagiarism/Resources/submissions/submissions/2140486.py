daybirth = input("Geef een string: ")
monthbirth = input("Geef een string: ")
yearbirth = input("Geef een string: ")
daynow = input("Geef een string: ")
monthnow = input("Geef een string: ")
yearnow = input("Geef een string: ")
if monthbirth - monthnow < 0:
    print(yearnow-yearbirth)
else:
    print(yearnow-yearbirth-1)
    