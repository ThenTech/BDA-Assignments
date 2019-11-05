word = input("Geef een zin in : ")
count = 0

for x in "abcdefghijklmnopqrstuvwxyz":
    for y in range(0, len(word)):
        if word[y] == x:
            count += 1
    print(x, ": ", count, sep="")
    count = 0