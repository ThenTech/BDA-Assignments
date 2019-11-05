day1 = int(input())
month1 = int(input())
year1 = int(input())
day2 = int(input())
month2 = int(input())
year2 = int(input())

age = year2 - year1 - 1

if month2 > month1 or (month1 == month2 and day2>=day1):
    age += 1

print(age)