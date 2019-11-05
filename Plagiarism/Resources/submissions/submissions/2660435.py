alfabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
teller = 0
woord = ""
for i in range(len(string)):
    kar = string[i]
    if kar in alfabet:
        teller += 1
        woord += kar
    elif i != 0 and (string[i-1] in alfabet or i == len(string)-1):
        print(woord,teller)
        woord = ""
        teller = 0
    else:
        woord = ""
        teller = 0