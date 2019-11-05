year = int(input("Give a year you want to check:"))

if year % 100 == 0 and year % 400 != 0:
    print(year, " is not a leap year")

elif year % 4 == 0:
    print(year, " is a leap year")

else:
    print(year, " is not a a leap year")