# write your code here

a_string = input("Give me a string: ")
string_len = len(a_string)
err = False

for index in range(string_len // 2):
    if not (a_string[index] == a_string[string_len - 1 - index]):
        err = True
    
if err:
    print(a_string, "is not a palindrome")
else:
    print(a_string, "is a palindrome")