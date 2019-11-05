string = input('String ')
lijst_string = list(string)
omgekeerd = ""
for el in range(len(string)):
    omgekeerd = omgekeerd + lijst_string[len(string)-1-el]
if omgekeerd == string:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")