birth_day = int(input("give day of birth: "))
birth_month = int(input("give month of birth: "))
birth_year = int(input("give year of birth: "))


current_day = int(input("give current day: "))
current_month = int(input("give current month: "))
current_year = int(input("give current year: "))


age = current_year - birth_year

if current_month == birth_month and current_day - birth_day < 0:
    age = age - 1

elif current_month - birth_month < 0:
    age = age - 1

print(age)