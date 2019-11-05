# write your code here
year=int(input("year"))
if  year%100==0 and not(year%400==0):
    print(str(year) + " is not a leap year")
elif year%4==0:
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")