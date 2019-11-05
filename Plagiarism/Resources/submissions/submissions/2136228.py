# write your code here
word = input("Give a word: ")
word_len = len(word)

for index in range(word_len):
    print(word[word_len - 1 - index], end="")