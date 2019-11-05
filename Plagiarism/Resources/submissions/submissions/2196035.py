# write your code here
string = input()
tekens = "0123456789,?;.:/!"
new=""
for i in range(len(string)):
    if string[i] not in tekens:
        new += string[i]
string = new.split()
lengthe = len(string)
for i in range(lengthe):
    print(string[i], len(string[i]))
