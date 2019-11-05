day1 = input()
month1 = input()
year1 = input()
day2 = input()
month2 = input()
year2 = input()

age = year2 - year1 - 1

if month2>month1 or (month1 == month2 and day2>=day1):
    age += 1

print(age)