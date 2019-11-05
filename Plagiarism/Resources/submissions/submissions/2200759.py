year = int(input("Enter the year"))

if year%4:
    if year%100:
        if year%400:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")