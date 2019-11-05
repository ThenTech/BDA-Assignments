# write your code here

year = int(input("input year: "))

if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not at leap year")
