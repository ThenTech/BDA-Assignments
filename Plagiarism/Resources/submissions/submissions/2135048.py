word = input("Give a word: ")
length = len(word)
i = length - 1

while i >= 0:
    number = length - (length - i)
    i = i - 1
    print(word[number], end="")
