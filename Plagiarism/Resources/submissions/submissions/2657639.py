int = input("")

list = []
for i in int:
    list.append(i)
list.reverse()
string = ""
for i in list:
    string += i
print(string)