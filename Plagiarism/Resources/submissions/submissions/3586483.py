word = input("Give a word")
alpha = "abcdefghijklmnopqrstuvwxyz"


for char in alpha:
    count = 0
    for j in range(0, len(word)):
        if (char == word[j]):
            count += 1
    print(char, count, sep=": ")