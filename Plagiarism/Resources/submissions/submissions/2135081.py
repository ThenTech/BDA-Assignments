year = input("give me a year")
year = int year

if (year%4)==0:
    if year%100 == 0:
        if year%400 == 0:
            print (year, "is a laep year")
        else 
        print (year, "is not a leap year")
    else 
        print (year, "is a leap year")
else 
        print (year, "is not a leap year")