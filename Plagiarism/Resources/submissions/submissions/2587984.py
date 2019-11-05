input = int(input(""))

if input % 4 == 0:
    if input % 100 == 0:
        if input % 400 == 0:
            print(input, "is a leap year")
        else:
            print(input, "is not a leap year")
    else:
        print(input, "is a leap year")
else:
    print(input, "is not a leap year")