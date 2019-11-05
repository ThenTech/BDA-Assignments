input1 = input("")
input2 = input("")

alfabet = "abcdefghijklmnopqrstuvwxyz"
list = []
for i in range(len(alfabet)):
    list.append(0)
for i in input1:
    for j in range(len(alfabet)):
        if alfabet[j] == i:
            list[j] += 1

list2 = []
for i in range(len(alfabet)):
    list2.append(0)
for i in input2:
    for j in range(len(alfabet)):
        if alfabet[j] == i:
            list2[j] += 1

if list2 == list:
    print(input1, "and", input2, "are anagrams")