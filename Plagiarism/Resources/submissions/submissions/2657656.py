int = input("")

list = []
for i in int:
    list.append(i)
list.reverse()
string = ""
for i in list:
    string += i
if string == int:
    print(int, "is a palindrome")
else:
    print(int, "is not a palindrome")