bday = int(input())
bmonth = int(input())
byear = int(input())
cday = int(input())
cmonth = int(input())
cyear = int(input())

year = 0
if cmonth < bmonth:
    year -= 1
if cmonth == bmonth:
    if cday < bday:
        year -= 1
year += (cyear - byear)