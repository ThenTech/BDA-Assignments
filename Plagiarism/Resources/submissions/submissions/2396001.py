birth_day = int(input("Birth day: "))
birth_month = int(input("Birth month: "))
birth_year = int(input("Birth year: "))

current_day = int(input("Current day: "))
current_month = int(input("Current month: "))
current_year = int(input("Current year: "))

"""
if birth_month == 1:
    one = birth_month
elif birth_month == 2:
    two = birth_month
elif birth_month == 3:
    three = birth_month
elif birth_month == 4:
    four = birth_month
elif birth_month == 5:
    five = birth_month
elif birth_month == 6:
    six = birth_month
elif birth_month == 7:
    seven = birth_month
elif birth_month == 8:
    eight = birth_month
elif birth_month == 9:
    nine = birth_month
elif birth_month == 10:
    ten = birth_month
elif birth_month == 11:
    eleven = birth_month
elif birth_month == 12:
    twelve = birth_month
"""

long = [1, 3, 5, 7, 8, 10, 12]      #31 days
short = [4, 6, 9, 11]               #30 days
leap = [2]                          #28-29 days

#amount_days = 0
if current_month == long:
    amount_days = 31
elif current_month == short:
    amount_days = 30
elif current_month == leap:
    amount_days = 28.25

day = current_day - birth_day
if day < 0:
    current_day += amount_days
    day = current_day - birth_day
#print(day)


month = current_month - birth_month
if month < 0:
    current_month += 1
    current_year -= 1
    day = current_month - birth_month
#print(month)


year = current_year - birth_year
if year < 0:
    day = current_year - birth_year
print(year)