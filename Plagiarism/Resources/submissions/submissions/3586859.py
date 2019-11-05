# write your code here
word = input("give a word ")
a=0

for i in range(len(word)):
    if word[i]!=(word[len(word)-1-i]):
        a=1

if(a==0):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")