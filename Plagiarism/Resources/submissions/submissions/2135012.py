string = input("String: ")
reversed_string = ""
i = -1

while -i <= len(string):
    reversed_string += string[i]
    i -= 1

if string == reversed_string:
    print("{string} is a palindrome".format(string=string))
else:
    print("{string} is not a palindrome".format(string=string))