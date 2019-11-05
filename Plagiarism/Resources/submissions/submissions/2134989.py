jaar = int(input("Geef een jaar: "))
if jaar % 100 == 0 and not jaar % 400 == 0:
    print(jaar, "is not a leap year")
elif jaar % 4 == 0:
    print(jaar, "is a leap year")