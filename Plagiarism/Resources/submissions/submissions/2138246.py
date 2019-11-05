day_1 = int(input("Birthday: "))
month_1 = int(input("Birth month: "))
year_1 = int(input("Birth year: "))

day_2 = int(input("Current day: "))
month_2 = int(input("Current month: "))
year_2 = int(input("Current Year"))

age = year_2 - year_1
if month_2 < month_1:
    age -= 1
elif day_2 < day_1:
    age -= 1

print(age)