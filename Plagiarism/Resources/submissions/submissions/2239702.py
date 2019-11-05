string = input("Geef een string op: ")

inword = False
count = 0
endcounter = 0
for x in string:
    if "a" <= x <= "z" or "A" <= x <= "Z":
        count = count+1
        print(x, end="")
        inword = True
    else:
        if inword:
            print("", count)
            count = 0
            inword = False
    endcounter = endcounter + 1
    if endcounter == len(string) and ("a" <= x <= "z" or "A" <= x <= "Z"):
        print("", count)