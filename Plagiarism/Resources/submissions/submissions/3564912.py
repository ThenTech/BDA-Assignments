birth_day = input("Date of birth\nday: ")
birth_month = input("month: ")
birth_year = input("year: ")

current_day = input("Current date\nday: ")
current_month = input("month: ")
current_year = input("year: ")

long = [1, 3, 5, 7, 8, 10, 12]
short = [4, 6, 9, 11]
leap = [2]

amount_days = 0
if current_month in long:
    amount_days = 31
elif current_month in short:
    amount_days = 30
elif current_month in leap:
    amount_days = 28.25

day = int(current_day) - int(birth_day)
if day < 0:
    current_day = int(current_day) + int(amount_days)
    day = int(current_day) - int(birth_day)

month = int(current_month) - int(birth_month)
if month < 0:
    current_month = int(current_month) + 1
    current_year = int(current_year) - 1
    month = int(current_month) - int(birth_month)

year = int(current_year) - int(birth_year)
if year < 0:
    year = int(current_year) - int(birth_year)

print(year)
