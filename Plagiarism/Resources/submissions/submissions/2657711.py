input = input("")

alfabet = "abcdefghijklmnopqrstuvwxyz"
list = []
for i in range(len(alfabet)):
    list.append(0)
for i in input:
    for j in range(len(alfabet)):
        if alfabet[j] == i:
            list[j] += 1
for i in range(len(alfabet)):
    print(alfabet[i] + ":", list[i])