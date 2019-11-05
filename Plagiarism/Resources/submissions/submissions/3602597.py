day1 = int(input(""))
month1 = int(input(""))
year1 = int(input(""))
day2 = int(input(""))
month2 = int(input(""))
year2 = int(input(""))
if year2 < 0 and year1 < 0:
    year2 *= -1
    year1 *= -1
if year2 < 0 and year1 > 0:
    age = (year2 * -1) + year1
elif year2 > 0 and year1 < 0:
    age = year2 + (year1 * -1)
elif year1 > year2:
    age = year1 - year2
else:
    age = year2 - year1
if month1 > month2:
    age -= 1
if month1 == month2 and day1 > day2:
    age -= 1

print(age)