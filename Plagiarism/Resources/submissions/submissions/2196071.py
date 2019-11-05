# write your code here
string = input()
tekens = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
new=""
for i in range(len(string)):
    if string[i] in tekens:
        new += string[i]
    else: 
        new += " "
string = new.split()
lengthe = len(string)
for i in range(lengthe):
    print(string[i], len(string[i]))
