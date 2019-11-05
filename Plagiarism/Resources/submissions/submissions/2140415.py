birthday = input("what day of the month where you born on?")
birthday = int(birthday)
birthmonth = input("what month where you born on?")
birthmonth = int(birthmonth)
birthyear = input("what year where you born in?")
birthyear = int(birthyear)

day = input("what day of the month is it?")
day = int(day)
month = input("what month is it?")
month = int(month)
year = input("what year is it?")
year = int(year)

output = year - (birthyear + 1)

if birthday + birthmonth * 30 <= day + month * 30:
	output += 1
print(output)
