bday = int(input(""))
bmonth = int(input(""))
byear = int(input(""))
day = int(input(""))
month = int(input(""))
year = int(input(""))

yearold = year - byear

if month < bmonth:
	yearold -= 1

if month == bmonth:
	dayold = day - bday
	if dayold < 0:
		yearold -= 1

print(yearold)
