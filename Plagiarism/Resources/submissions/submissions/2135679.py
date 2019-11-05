from datetime import date
Day1 = int(input("Give start day: "))
Month1 = int(input("Give start month: "))
Year1 = int(input("Give start year: "))
Day2 = int(input("Give end day: "))
Month2 = int(input("Give end month: "))
Year2 = int(input("Give end year: "))
f_date = date(Year1, Month1, Day1)
l_date = date(Year2, Month2, Day2)
delta = l_date - f_date
print(int(delta.days / 365))
