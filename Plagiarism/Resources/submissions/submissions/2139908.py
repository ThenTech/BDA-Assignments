year = int(input())
if (year % 4 == 0):
    if(year % 100 == 0):
        if (year % 400 == 0):
            print(year, " is a leap year")
        print(year, " is not a leap year")
    print(year, " is aleap year")
print(year, " is not a leap year")