# write your code here
a=int(input("day you were born"))
b=int(input("month you were born"))
c=int(input("year you were born"))
d=int(input("current day"))
e=int(input("current month"))
f=int(input("current year"))

if  b==e and a>=d:
   print(f-c)
elif e>=b:
    print(f-c)
else:
    print(f-c-1)