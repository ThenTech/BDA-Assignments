word = input('word?')
reverse = ''
i = len(word) - 1
while i >= 0:
    reverse += word[i]
    i -= 1
print(reverse)
