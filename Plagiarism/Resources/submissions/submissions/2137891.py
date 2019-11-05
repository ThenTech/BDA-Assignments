word = str(input("Word:"))
n = len(word)
while n != 0:
    print(word[n-1], end="")
    n -= 1