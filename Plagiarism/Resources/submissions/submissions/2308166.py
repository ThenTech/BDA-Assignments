days = int(input())
hours = int(input())

minutes_days = days * 24 * 60
minutes_hours = 60 * hours
minutes = minutes_days + minutes_hours
print(minutes)