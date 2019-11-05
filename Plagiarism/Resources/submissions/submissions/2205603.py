s = input("")
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
newstring = ""

for i in range(len(s)):
    if s[i] in alpha:
        newstring += s[i]
    else:
        newstring += " "

newstring = newstring.split()

for i in range(len(newstring)):
    print(newstring[i], len(newstring[i]))