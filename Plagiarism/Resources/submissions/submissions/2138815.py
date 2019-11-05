day_of_birth = int(input())
month_of_birth = int(input())
year_of_birth = int(input())

day_of_today = int(input())
month_of_today = int(input())
year_of_today = int(input())

if day_of_today - day_of_birth < 0:
    month_of_birth += 1

if month_of_today - month_of_birth < 0:
    year_of_birth += 1

print(year_of_today - year_of_birth)