day_1 = int(input("Give a day: "))
month_1 = int(input("Give a month: "))
year_1 = int(input("Give a year: "))

day_2 = int(input("Give a second day: "))
month_2 = int(input("Give a second month: "))
year_2 = int(input("Give a second year: "))

if (day_2 >= day_1 and month_2 >= month_1 and year_2 >= year_1):
    age = year_2 - year_1
elif(year_1 == year_2):
    age = 0
else:
    age = year_2 - year_1 - 1

print(age)