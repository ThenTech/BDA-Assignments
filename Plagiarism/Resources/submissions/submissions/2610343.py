# write your code here
word=input("give a word")

reverse=""
for i in range(len(word)):
    reverse+=word[len(word)-1-i]
    
print(reverse)
    
