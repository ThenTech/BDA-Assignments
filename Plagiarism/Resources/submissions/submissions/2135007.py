# the year is divisible by 4, unless it is divisible by 100 and not by 400

x = int(input("Give me a year:"))

if (x % 4 == 0):
    if (x % 100 == 0 and x % 400 != 0):
        print(x, "is not a leap year")

    else:
        print(x, "is a leap year")