year = int(input("Year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("{year} is not a leap year".format(year=year))
    else:
        print("{year} is a leap year".format(year=year))

elif year % 4 == 0:
    print("{year} is a leap year".format(year=year))