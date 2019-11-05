x = int(input("Year: "))

if x % 4 == 0:
    if x % 100 == 0 and not(x % 400 == 0):
        print(x, "is not a leap year")
    else:
        print(x, "is a leap year")