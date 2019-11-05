x = int(input("x"))


if (x % 4 == 0):
    if x % 100 == 0:
        if x % 200 == 0:
            print(x, "is a leap year")
        else:
            print(x, "is not a leap year")
    else:
        print(x, "is a leap year")
else:
    print(x, "is not a leap year")