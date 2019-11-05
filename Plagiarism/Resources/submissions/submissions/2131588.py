response_days = input("How many days?")
response_hours = input("How many hours?")
days = int(response_days)
hours = int(response_hours)

days_in_min = days * 24 * 60
hours_in_min = hours * 60

total_min = days_in_min + hours_in_min

print(total_min)