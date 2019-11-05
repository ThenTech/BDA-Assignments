x = input("word?")
counter = 0

for i in "abcdefghijklmnopqrstuvwxyz":
    for j in x:
        if j != i:
            continue
        else:
            counter = counter+1
    print(i, ": ", counter, sep="")
    counter = 0