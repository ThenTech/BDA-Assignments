days = int(input("Number of days: "))
hours = int(input("Number of minutes: "))
MinDays = (days * 24) * 60
MinHours = hours * 60
TotalMinutes = MinDays + MinHours
print(TotalMinutes)