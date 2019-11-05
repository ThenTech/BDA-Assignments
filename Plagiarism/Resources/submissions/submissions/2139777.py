birth_day = int(input("Day of birth:"))
birth_month = int(input("Month of birth:"))
birth_year = int(input("Year of birth:"))

day_now = int(input("Today:"))
month_now = int(input("Current month:"))
year_now = int(input("Current year:"))

if (day_now > birth_day):
    birth_month = birth_year + 1
    if month_now > birth_month:
        birth_year = birth_year + 1

age = year_now - birth_year
print(age)