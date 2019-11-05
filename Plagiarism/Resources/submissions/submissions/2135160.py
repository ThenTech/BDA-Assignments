# write your code here

word = input("word: ")
i = 0


while i+1 < len(word):
    if word[i] != word[len(word) - 1 - i]:
        print(word, "is not a palindrome")
        break
    elif i+1 == len(word):
        print(word, "is a palindrome")