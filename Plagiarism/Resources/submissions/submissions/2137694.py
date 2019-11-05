word=input("give a word: ")
for reverse in range(ln(word)):
    print(word[len(word)-1-reverse],end="")