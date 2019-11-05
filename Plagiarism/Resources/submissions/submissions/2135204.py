word = input()
i = 0
while i < len(word):
    print(str(word[len(word) - 1 - i]), end="")
    i += 1
print("")