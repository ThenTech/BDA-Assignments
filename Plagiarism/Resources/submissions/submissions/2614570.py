input = input("")
string = ""
lengte = 0
woord = ""
spatie = False
for i in input:
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        string += i
        spatie = False
    elif spatie == False:
        spatie = True
        string += " "
for i in range(len(string)):
    if string[i] == " ":
        print(woord, lengte)
        lengte = 0
        woord = ""
        continue
    woord += string[i]
    lengte += 1
    if i == len(string)-1:
        print(woord, lengte)
