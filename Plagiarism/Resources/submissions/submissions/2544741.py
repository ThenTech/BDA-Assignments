J = int(input("Jaartal: "))

if (J % 4 == 0) and (J % 100 != 0 or J % 400 == 0):
    print(J, "is a leap year")
else:
    print(J, "is not a leap year")