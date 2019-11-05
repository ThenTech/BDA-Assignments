x = int(input("Geef een jaartal:"))
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print(x, "is a leap year")
elif (x % 4 != 0) or (x % 4 == 0 and x % 100 == 0):
    print(x, "is not a leap year")
