bday = int(input("Birthday = ?\n"))
bmonth = int(input("Birthmonth = ?\n"))
byear = int(input("Birthyear = ?\n"))

curday = int(input("Current day = ?\n"))
curmonth = int(input("Current month = ?\n"))
curyear = int(input("Current year = ?\n"))

age = 0

if curmonth <= bmonth:
    if curday < bday:
        age = curyear - byear - 1
    else:
        age = curyear - byear
else:
    age = curyear - byear

if curyear > 0 and byear < 0:
    age -= 1

print(age)
