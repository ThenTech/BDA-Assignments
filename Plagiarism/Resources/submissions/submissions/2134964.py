year = int(input(""))
not_leap = year % 100
leap = year % 4
leap400 = year % 400
if leap400 == 0:
    print(year, "is a leap year")

elif not_leap == 0:
    print(year, "is not a leap year")

elif leap == 0:
    print(year, "is a leap year")


else:
    print(year, "is not a leap year")
