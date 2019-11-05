day1 = int(input("enter the day"))
month1 = int(input("enter the month"))
year1 = int(input("enter the year"))
day2 = int(input("enter the day"))
month2 = int(input("enter the month"))
year2 = int(input("enter the year"))

mtd1 = month1 * 30
mtd2 = month2 * 30
if year1 >= 0:
    ytd1 = year1 * 365
else:
    ytd1 = -year1 * 365
if year2 >= 0:
    ytd2 = year2 * 365
else:
    ytd2 = -year2 * 365
days1 = day1 + mtd1 + ytd1
days2 = day2 + mtd2 + ytd2

age = int((days2 - days1) / 360)
if year1<0 or year2<0:
    print(-age)
else:    
    print(age)