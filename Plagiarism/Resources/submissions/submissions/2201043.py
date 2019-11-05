string = input("input a string please")
reverse = ""
i = len(string)

while i>0:
    reverse += string[i-1]
    i -= 1
print(reverse)