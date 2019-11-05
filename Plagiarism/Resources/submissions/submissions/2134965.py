jaar = int(input("Geef een jaar: "))

if jaar % 4 == 0:
    if (jaar % 100 == 0) and not(jaar % 400 == 0):
        print(jaar, "is a not leap year")
    else:
        print(jaar, "is a leap year")
else:
    print(jaar, "is not a leap year")