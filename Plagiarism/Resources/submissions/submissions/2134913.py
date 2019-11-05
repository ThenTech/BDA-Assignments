word = input("write the word here")
x = len(word)-1
if len(word)!=0:
    while x >= 0:
        print(word[x], end="")
        x -= 1
print()