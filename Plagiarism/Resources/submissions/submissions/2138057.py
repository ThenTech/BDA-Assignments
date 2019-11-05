word = input("please enter a word")
drow = ""
for i in range(len(word)):
    drow += word[len(word)-(i+1)]
if(drow == word):
	print(drow, "is a pallindrome")
else:
	print(word, "is not a pallindrome")