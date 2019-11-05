string123 = input()
lengte = 0
string = ""
for i in range(len(string123)-1):
    if "a"<=string123[i]<="z" or "A"<=string123[i]<="Z":
        lengte+=1
        string += string123[i]
    if lengte != 0 or len(string123)-1 = i:
        print(string+" "+str(lengte))
        lengte = 0
        string = ""