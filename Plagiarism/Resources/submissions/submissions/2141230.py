word = str(input("Give a word "))
for i in range(len(word)):
    print(word[len(word) - 1 - i], end="")
print()