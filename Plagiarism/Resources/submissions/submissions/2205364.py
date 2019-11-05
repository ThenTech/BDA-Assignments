t = s.split()

for i in t:
    newstring = ""
    for j in range(len(i)):
        if "A" <= i[j] <=  "Z" or "a" <= i[j] <= "z":
            newstring += i[j]
    if newstring != "":
        print(newstring, len(newstring))