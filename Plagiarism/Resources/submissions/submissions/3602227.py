# write your code here
word = input("Give me a word")

for i in range(0, len(word)):
    print(word[len(word) - i - 1], end="")