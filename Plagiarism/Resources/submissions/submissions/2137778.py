checkYear = int(input())
if(checkYear%4 == 0 and not(checkYear%100 == 0 and not(checkYear%400 == 0))):
    print(checkYear, "is a leap year")
else:
    print(checkYear, "is not a leap year")
