word = input("Word = ?\n")
drow = ""

for i in range(len(word), 0, -1):
    drow = drow + word[i-1]

print(drow)
