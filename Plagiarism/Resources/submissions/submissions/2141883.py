# Andere oplossing
word = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"

for char in alphabet:
    count = 0
    for j in range(0, len(word)):
        if (char == word[j]):
            count = count + 1
    print(char, count, sep=": ")