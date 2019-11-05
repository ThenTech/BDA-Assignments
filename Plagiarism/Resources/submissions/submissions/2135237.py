s = input()
palindrome = True

i = 0
while (i < len(s)/2):
    if not(s[i] == s[len(s)-1-i]):
        palindrome == False
        break
    i +=1
        
if palindrome:
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')