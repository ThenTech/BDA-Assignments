days = int(input("How many days?"))
hours = int(input("hours?"))

days_in_minutes = days*24*60
hours_in_minutes = hours*60
total_minutes = days_in_minutes + hours_in_minutes

print(total_minutes)