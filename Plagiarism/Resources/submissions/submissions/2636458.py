birth_day = int(input(""))
birth_month = int(input(""))
birth_year = int(input(""))
current_day = int(input(""))
current_month = int(input(""))
current_year = int(input(""))

leeftijd = current_year - birth_year
if (current_day + 31*current_month) < (birth_day + 31*birth_month):
    leeftijd -= 1

print(leeftijd)