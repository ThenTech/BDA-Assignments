# write your code here
word=input("give a word")
palindrome=""
for i in range (len(word)):
    palindrome =(word[len(word) -1 -i])
if word == palindrome:
    print(word, " is a palindrome")
else:
    print(word, "is not a palindrome")