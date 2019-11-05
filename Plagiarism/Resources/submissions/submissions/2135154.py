year = int(input())
x = True
while year > 0:
    if year % 400 == 0 and year % 100 == 0:
        print(year,"is a leap year")

    else:
        x = False

    if year % 4 == 0 and x == True:
        print(year, "is a leap year")

    else:
        print(year, "is not a leap year")
    year = int(input())