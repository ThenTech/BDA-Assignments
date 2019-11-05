# Write a program that takes two dates as input, a birth date and the current date (each consisting of three numbers,
#  a day, a month, and a year) and calculates the age of persons born at the specified birthdate.

birth_date_day = int(input("geef de geboortdatum dag: "))
birth_date_month = int(input("Geef de geboortedatum maand (in cijfers): "))
birth_date_year = int(input("geef de geboortedatum jaar: "))

current_day = int(input("Geef dag in van vandaag: "))
current_month = int(input("geef huidige maand in (in cijfers: "))
current_year = int(input("geef huidig jaar in: "))

year = current_year - birth_date_year
month = current_month - birth_date_month
day = current_day - birth_date_day

if month < 0:
    age = year - 1
elif day < 0 and month == 0:
    age = year - 1
else:
    age = year

print(age)
