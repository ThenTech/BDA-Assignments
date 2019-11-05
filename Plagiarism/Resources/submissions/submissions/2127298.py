days = input("Amount of days = ")
hours = input("Amount of hours = ")

days = int(days)
hours = int(hours)

min_day = days * 24 * 60
min_hour = hours * 60

total = min_day + min_hour
total = str(total)
print(total)
