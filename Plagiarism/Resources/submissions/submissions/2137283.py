word = input("Geef een string op : ")

for x in range(0,len(word)):
    print(word[len(word)-x-1], end="")
