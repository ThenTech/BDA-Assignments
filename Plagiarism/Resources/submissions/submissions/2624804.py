string123 = input()
lengte = 0
string = ""
for i in string123:
    if "a"<=i<="z" or "A"<=i<="Z":
        lengte+=1
        string += i
    elif lengte != 0:
        print(string+" "+lengte)
        lengte = 0
        string = ""