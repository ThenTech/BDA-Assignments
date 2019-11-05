word = input()
pos = 0
while pos < len(word):
    print(word[len(word) - pos - 1], end="")
    pos+=1