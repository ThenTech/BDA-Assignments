x3 = int(input("Day?"))
x2 = int(input("Month?"))
x1 = int(input("Year?"))

y3 = int(input("Day?"))
y2 = int(input("Month?"))
y1 = int(input("Year?"))

a1 = y1 - x1

#-1
if x2 > y2:
        print(a1-1)
elif x2 > y2:
    if x3 >= y3:
        print(a1)
    else:
        print(a1-1)
#0
else:
    print(a1)