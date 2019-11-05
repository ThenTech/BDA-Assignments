word = input("give a word: ")
for reverse in range(len(word)):
    print(word[len(word)-1-reverse], end="")