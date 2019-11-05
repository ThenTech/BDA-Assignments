year = int(input(""))

leap = year % 4

if leap == 0:
	print(year, "is a leap year")

else:
	print(year, "is not a leap year")
