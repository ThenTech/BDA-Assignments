string = input("")
woord = False
teller = 0
y = ""
for x in string:
    if "a" <= x <= "z" or "A" <= x <= "Z":
        teller +=1
        y = y + x
    else:
        if teller == 0:
            continue
        print(y, teller, sep=" ")
        y = ""
        teller = 0
        continue
print(y, teller, end=" ")