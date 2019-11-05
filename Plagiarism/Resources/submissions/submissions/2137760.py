day_birth = int(input())
month_birth = int(input())
year_birth = int(input())
day_now = int(input())
month_now = int(input())
year_now = int(input())

day = day_now - day_birth
if day < 0:
    month_birth += 1
month = month_now - month_birth
if month < 0:
    year_birth =+ 1
year = year_now - year_birth
print(str(year))