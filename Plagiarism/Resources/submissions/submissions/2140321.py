day = int(input(""))
month = int(input(""))
year = int(input(""))
cday = int(input(""))
cmonth = int(input(""))
cyear = int(input(""))
monthdays = month * 30
yeardays = year * 365
cmonthdays = cmonth * 30
cyeardays = cyear * 365
difference = (cday + cmonthdays + cyeardays)-(day + monthdays + yeardays)
newyear = difference // 365
newmonth = (difference - (newyear * 365))//12
newday = (difference - (newyear * 365) - (newmonth * 12))//30
print(newyear)
print(newmonth)
print(newday)