# write your code here
year = int(input())
if year % 4 == 1:
    print(year,"is not a leap year")
elif year % 100 == 0:
    if year % 400 ==0:
        print(year, "is a leap year")
    else:
        print(year,"is not a leap year")
else: 
    print(year,"is a leap year")