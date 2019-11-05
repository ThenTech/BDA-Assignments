year = input("Geef jaar in: ")
if int(year) % 100 == 0 and int(year) % 400 != 0:
    print(year, "is not a leap year")
elif int(year) % 4 != 0:
    print(year, "is a not leap year")
else:
    print(year, "is a leap year")