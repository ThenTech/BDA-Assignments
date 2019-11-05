day_born = int(input("day born: "))
month_born = int(input("month born: "))
year_born = int(input("year born: "))

day_now = int(input("current day: "))
month_now = int(input("current month: "))
year_now = int(input("current year: "))

year = year_now - year_born
month = month_now - month_born
day = day_now - day_born

age = year

if month_now < month_born:
    age = year - 1
else:
    age = year

if day_now < day_born:
    age = year - 1
else:
    age = year

print(age)