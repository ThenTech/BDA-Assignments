year = int(input("Enter the year"))

if not(year%4):
    if not(year%100):
        if not(year%400):
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")