word = input("give a word: ")

length_word = len(word)

for i in range(length_word):
    print(word[length_word - 1 - i], end="")
print()