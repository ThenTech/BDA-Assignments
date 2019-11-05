word = input("Give a word: ")
length = len(word)
i = length - 1
reverse = ""
while i >= 0:
    number = length - (length - i)
    i = i - 1
    reverse = reverse + word[number]
print(reverse)