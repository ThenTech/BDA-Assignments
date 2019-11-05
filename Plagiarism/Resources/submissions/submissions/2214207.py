days = int(input("days: "))
hours = int(input("hours: "))

day_minutes = days * 24 * 60
hours_minutes = hours * 60
x = day_minutes + hours_minutes
print(x)
