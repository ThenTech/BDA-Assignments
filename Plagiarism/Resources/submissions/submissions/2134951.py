year = input("Year = ?\n")

if int(year) % 4 != 0 or (int(year) % 100 == 0 and not int(year) % 400 == 0):
    print(year + " is not a leap year")
else:
    print(year + " is a leap year")
