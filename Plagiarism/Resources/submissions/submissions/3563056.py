year = int(input("Give a year: "))


if (year % 400 != 0):
    pass
elif (year % 4 == 0 ):
    print(year, "is a leap year")