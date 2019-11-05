# write your code here
response = input("Year?")
x = int(response)

if (x % 400 == 0):
    print (x, " is  leap year" )
elif (x % 4 == 0 and x % 100 != 0):
    print (x, " is  leap year")
else:
    print (x, " is not leap year")