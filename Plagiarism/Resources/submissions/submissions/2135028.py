jaar = int(input("Geef een jaar: "))
if jaar % 4 == 0:
    print(jaar, "is a leap year")
elif jaar % 100 == 0 and jaar % 400 != 0:
    print(jaar, "is a leap year")
else:
    print(jaar, "is not a leap year")