word = input()
i = len(word) - 1
reversed_word = ""
while i >= 0:
    reversed_word += word[i]
    i -= 1
print(reversed_word)