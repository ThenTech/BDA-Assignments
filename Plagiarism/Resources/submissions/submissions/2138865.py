word = input("Give word: ")
i = len(word)-1
reverse = ""

while i >= 0:
    reverse += word[i]
    i -= 1

print(reverse)
