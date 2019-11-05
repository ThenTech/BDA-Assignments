day1 = input("")
month1 = input("")
year1 = input("")
day2 = input("")
month2 = input("")
year2 = input("")
if year2 < 0:
    year2 *= -1
if year1 < 0:
    year1 *= -1
age = year2 - year1
if month1 > month2:
    age -= 1
if month1 == month2 and day1 > day2:
    age -= 1
print(age)