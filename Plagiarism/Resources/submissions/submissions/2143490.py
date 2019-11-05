import math

text = input()

length = len(text)
isPalindrome = True

for i in range(0, math.ceil(length/2)):
    if text[i] != text[(length-1)-i]:
        isPalindrome = False

if isPalindrome:
    print(text + " is a palindrome")
else:
    print(text + " is not a palindrome")