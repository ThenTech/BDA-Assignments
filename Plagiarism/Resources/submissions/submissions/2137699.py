string = str(input("Input your word here: "))
if string == "":
    print("")
for i in range(len(string)):
    print(string[len(string)-1-i], end="")