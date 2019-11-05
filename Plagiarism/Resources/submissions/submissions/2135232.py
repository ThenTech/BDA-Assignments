s = input()
palindrome = True

i = 0
while (palindrome == True and i < len(s)/2):
    if not(s[i] == s[len(s)-1-i]):
        palindrome == False
        
if palindrome:
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')