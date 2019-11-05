y = int(input("FIll in a year to check: "))
if y == 1900:
    print(y, "is not a leap year")
elif y%100==0 and y%400!=0:
    print(y, "is not a leap year")
elif y%4==0:
    print(y, "is a leap year")
else:
    print(y, "is not a leap year")
