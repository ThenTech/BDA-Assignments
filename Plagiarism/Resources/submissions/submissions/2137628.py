word = input("Geef een woord op : ")
y = 0
for x in range(0, len(word)):
    if word[x] == word[len(word)-x-1]:
        pass
    else:
        print(word, "is not a palindrome")
        y = 1
        break
if y == 0:
    print(word, "is a palindrome")