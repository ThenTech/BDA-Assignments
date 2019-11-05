day1 = input("Birthdate day")
month1 = input("Birthdate month")
year1 = input("Birthdate year")
day2 = input("day")
month2 = input("month")
year2 = input("year")

year1 = int(year1)
year2 = int(year2)
month1 = int(month1)
month2 = int(month2)
day1 = int(day1)
day2 = int(day2)

age = year2 - year1

if age < 0:
    age = age * -1
    
age += -1

if month2 > month1:
    age += 1
elif month2 == month1:
    if day2 >= day1:
        age += 1
print(age)