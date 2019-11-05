# write your code here
checkpal = input("Word?")
pal = ""
for i in range(len(checkpal)):
    pal = pal + checkpal[len(checkpal) - 1 - i]
if pal == checkpal:
    print(checkpal,"is a palindrome")
else:     
    print(checkpal,"is a palindrome")
