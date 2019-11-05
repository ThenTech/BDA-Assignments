i = int(input("Give a year"))

if i % 4 == 0:
    if i % 100 == 0 and not(i % 400 == 0):
        print(i, "is not a leap year")
    else:
        print(i, "is a leap year")