string = input("Geef een string op: ")

inword = False
count = 0
for x in string:
    if "a" <= x <= "z" or "A" <= x <= "Z":
        inword = True
        count = count+1
        print(x, end="")
    else:
        if inword:
            print("", count)
            count = 0
            inword = False
    if x == string[-1]:
        print("", count)