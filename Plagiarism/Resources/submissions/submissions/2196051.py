# write your code here
string = input()
string = string.lower()
tekens = "abcdefghijklmnopqrstuvwxyz"
new=""
for i in range(len(string)):
    if string[i] not in tekens:
        new += string[i]
    else: 
        new += " "
string = new.split()
lengthe = len(string)
for i in range(lengthe):
    print(string[i], len(string[i]))
