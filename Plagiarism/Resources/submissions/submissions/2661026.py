string = input()

isPalindrome = True

for x in range(int(len(string)/2)):
    if string[x] != string[len(string)-1-x]:
        isPalindrome = False
        break
    
if isPalindrome:
    print(string, 'is a palindrome')
else:
    print(string, 'is not a palindrome')