string = input("input a string please")
reverse = ""
i = len(string)

while i>0:
    reverse += string[i-1]
    i -= 1
if reverse == string:
    print(string,"is a palindrome")
else:
    print(string,"is not a palindrome")