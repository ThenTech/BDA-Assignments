birth_day = int(input("Birth day: "))
birth_month = int(input("Birth month: "))
birth_year = int(input("Birth year: "))

current_day = int(input("Day: "))
current_month = int(input("Month: "))
current_year = int(input("Year: "))

if current_month > birth_month:
    current_age = current_year - birth_year
elif current_month == birth_month and current_day >= birth_day:
    current_age = current_year - birth_year
else:
    current_age = current_year - birth_year - 1

print(current_age)