string = input("Geef een string")
palindrome = True
for i in range(len(string)//2):
    if string[i] != string[len(string)-i-1]:
        palindrome = False
if True:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")