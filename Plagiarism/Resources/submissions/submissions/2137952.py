word = input("please enter a word")
drow = ""
for i in range(len(word)):
    drow += word[len(word)-(i+1)]
print(drow)
