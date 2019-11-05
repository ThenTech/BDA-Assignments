string = input("Geef een string")
for i in range(len(string)):
    if string[i]= string[len(string)-i-1]:
        print(string, "is a palindrome")
    else: 
        print(string, "is not a palindrome")