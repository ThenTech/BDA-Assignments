x=int(input("Give a year: "))
if x%100==0 or x%4==0:
    print(x, "is a leap year.")
elif x%400==0:
        print(x,"isn't a leap year.")
else:
    print(x,"isn't a leap year.")