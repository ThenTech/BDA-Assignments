string = input("Geef een string op: ")

inword = False
count = 0
endcounter = 0
for x in string:
    if "a" <= x <= "z" or "A" <= x <= "Z":
        count = count+1
        endcounter = endcounter + 1
        print(x, end="")
        inword = True
    else:
        if inword:
            print("", count)
            count = 0
            endcounter = endcounter + 1
            inword = False
    if endcounter == len(string)-2:
        print("", count)