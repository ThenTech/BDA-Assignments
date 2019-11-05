string = str(input("Input your word here: "))
for i in range(len(string)):
    print(string[len(string)-1-i], end="")
print()