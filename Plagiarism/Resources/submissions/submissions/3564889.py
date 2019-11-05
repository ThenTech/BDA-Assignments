word = input("Give a single word: ")
if len(word) > 0:
    for i in range(len(word)):
        print(word[-i-1], end="")
