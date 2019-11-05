b_day = int(input("Give me the birthday. "))
b_month = int(input("Give me the birth month. "))
b_year = int(input("Give me the birth year. "))
c_day = int(input("Give me the current day. "))
c_month = int(input("Give me the current month. "))
c_year = int(input("Give me the current year. "))

age = 0


if b_year < c_year and b_day < c_day and b_month <= c_month:
    age = c_year - b_year - 1

elif b_year < c_year and b_day >= c_day and b_month >= c_month:
    age = c_year - b_year - 1

else:
    age = c_year - b_year

print(age)