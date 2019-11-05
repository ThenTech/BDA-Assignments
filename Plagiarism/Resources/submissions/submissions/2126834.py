days = int(input("Days: "))
hours = int(input("Hours: "))

minutes = 0
minutes += days * 24 * 60
minutes += hours * 60

print(minutes)