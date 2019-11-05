a = int(input("Enter the number of days: "))
b = int(input("Enter the #hours: "))
hours_in_minutes = b * 60
days_in_minutes = (a*24)*60
total = hours_in_minutes + days_in_minutes
print(total)